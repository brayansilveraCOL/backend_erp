# Import Local Models
from erp_backend.utils.models import Parameter

# Import Serializers
from erp_backend.utils.api.serializers.serializers_parameter import ParameterModelSerializer
# Import DRF
from rest_framework import mixins, viewsets

# Permission
from rest_framework.permissions import IsAdminUser


class ParameterViewSet(mixins.CreateModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.ListModelMixin,
                       mixins.DestroyModelMixin,
                       viewsets.GenericViewSet):
    serializer_class = ParameterModelSerializer
    queryset = Parameter.objects.filter(state=True)

    def get_permissions(self):
        """Assign permissions based on action."""
        permissions = [IsAdminUser]
        return [permission() for permission in permissions]

    def perform_destroy(self, instance):
        """Disable membership."""
        instance.state = False
        instance.save()


# Import Local Models
from erp_backend.utils.models import Iva

# Import Serializers
from erp_backend.utils.api.serializers.serializers_iva import IvaModelSerializer
# Import DRF
from rest_framework import mixins, viewsets

# Permission
from erp_backend.utils.permissions.utils import IsAdminPlatform
from rest_framework.permissions import IsAdminUser


class IvaViewSet(mixins.CreateModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.ListModelMixin,
                 mixins.DestroyModelMixin,
                 viewsets.GenericViewSet):
    serializer_class = IvaModelSerializer
    lookup_field = 'ano'
    queryset = Iva.objects.filter(state=True)

    def get_permissions(self):
        """Assign permissions based on action."""
        permissions = [IsAdminUser]
        return [permission() for permission in permissions]

    def perform_destroy(self, instance):
        """Disable membership."""
        instance.state = False
        instance.save()

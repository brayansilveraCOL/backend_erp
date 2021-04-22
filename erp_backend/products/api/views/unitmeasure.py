# Import Local Models
from erp_backend.products.models import UnitMeasure

# Import Serializers
from erp_backend.products.api.serializers.unitmeasure import UnitMeasureModelSerializer
# Import DRF
from rest_framework import mixins, viewsets

# Permission
from rest_framework.permissions import IsAdminUser


class UnitMeasureViewSet(mixins.CreateModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.ListModelMixin,
                         mixins.DestroyModelMixin,
                         viewsets.GenericViewSet):
    serializer_class = UnitMeasureModelSerializer
    queryset = UnitMeasure.objects.filter(state=True)
    lookup_field = 'UniqueCode'

    def get_permissions(self):
        """Assign permissions based on action."""
        permissions = [IsAdminUser]
        return [permission() for permission in permissions]

    def perform_destroy(self, instance):
        """Disable Iva."""
        instance.state = False
        instance.save()

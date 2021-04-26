# Model
from erp_backend.list_price.models import TypePlan

# Serializers
from erp_backend.list_price.api.serializers.typeplan import TypePlanModelSerializer

# DRF
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAdminUser


class TypePlanViewSet(mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.CreateModelMixin,
                      viewsets.GenericViewSet):
    serializer_class = TypePlanModelSerializer
    queryset = TypePlan.objects.filter(state=True)
    lookup_field = 'UniqueCode'

    def get_permissions(self):
        """Assign permissions based on action."""
        permissions = [IsAdminUser]
        return [permission() for permission in permissions]

    def perform_destroy(self, instance):
        """
        :param instance:
        :return:  Instance in False Logic Delete
        """
        instance.state = False
        instance.save()

# Model
from erp_backend.inventorys.type_movement_model import TypeMovement

# Serializers
from erp_backend.inventorys.api.serializers.typeMovement import TypeMovementModelSerializer

# DRF
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAdminUser


class TypeMovementViewSet(mixins.ListModelMixin,
                          mixins.RetrieveModelMixin,
                          mixins.CreateModelMixin,
                          mixins.UpdateModelMixin,
                          mixins.DestroyModelMixin,
                          viewsets.GenericViewSet):
    serializer_class = TypeMovementModelSerializer
    queryset = TypeMovement.objects.filter(state=True)
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



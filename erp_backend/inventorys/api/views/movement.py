# Serializers
from erp_backend.inventorys.api.serializers.movement import MovementModelSerializer, MovementCreateSerializer

# Models
from erp_backend.inventorys.models import Movement

# Rest Framework
from rest_framework.decorators import api_view
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAdminUser

from erp_backend.utils.functions.movement_internal_code import generate_code


class ListRetrieveMovementViewSet(mixins.ListModelMixin,
                                  mixins.RetrieveModelMixin,
                                  GenericViewSet):
    serializer_class = MovementModelSerializer
    queryset = Movement.objects.filter(state=True)
    lookup_field = 'uniqueCode'

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


@api_view(['POST'])
def api_view_movement(request):
    if request.method == 'POST':
        serializer = MovementCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

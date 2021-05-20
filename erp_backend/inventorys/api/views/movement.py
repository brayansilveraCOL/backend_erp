# Serializers
from erp_backend.inventorys.api.serializers.movement import MovementModelSerializer, MovementCreateSerializer, \
    MovementCancelSerializer

# Models
from erp_backend.inventorys.models import Movement

# Rest Framework
from rest_framework.decorators import api_view
from rest_framework import mixins, status
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


@api_view(['POST'])
def api_view_movement(request):
    if request.method == 'POST':
        serializer = MovementCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


@api_view(['DELETE'])
def api_view_detail_movement(request, UniqueCode=None):
    if UniqueCode:
        movement = Movement.objects.filter(uniqueCode=UniqueCode, state=True).first()
        if movement:
            if request.method == 'DELETE':
                data = {
                    "uniqueCode": UniqueCode
                }
                serializer = MovementCancelSerializer(movement, data=data, partial=True)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                print(serializer)
                serializer_movement = MovementModelSerializer(movement)
                return Response(serializer_movement.data, status=status.HTTP_202_ACCEPTED)
            else:
                return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)

    else:
        return Response(status=status.HTTP_204_NO_CONTENT)

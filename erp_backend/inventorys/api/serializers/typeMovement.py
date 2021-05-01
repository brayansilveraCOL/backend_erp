# Model
from erp_backend.inventorys.type_movement_model import TypeMovement

# DRF
from rest_framework import serializers


class TypeMovementModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = TypeMovement
        fields = '__all__'

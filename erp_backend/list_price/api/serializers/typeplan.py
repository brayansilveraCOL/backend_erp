# Model
from erp_backend.list_price.models import TypePlan

# DRF
from rest_framework import serializers


class TypePlanModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypePlan
        fields = '__all__'

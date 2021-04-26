# Model
from erp_backend.list_price.models import TypeSale

# DRF
from rest_framework import serializers


class TypeSaleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeSale
        fields = '__all__'

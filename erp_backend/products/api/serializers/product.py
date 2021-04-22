# Django Models
from erp_backend.products.models import Product, Category, UnitMeasure

# DRF
from rest_framework import serializers

# Serializers

from erp_backend.products.api.serializers.category import CategoryModelSerializer
from erp_backend.products.api.serializers.unitmeasure import UnitMeasureModelSerializer


class ProductModelSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.filter(state=True))
    unitMeasure = serializers.PrimaryKeyRelatedField(queryset=UnitMeasure.objects.filter(state=True))

    class Meta:
        model = Product
        fields = '__all__'

    def create(self, data):
        print(data)
        product = Product.objects.create(**data)
        return product


class ProductListModelSerializer(serializers.ModelSerializer):
    category = CategoryModelSerializer(read_only=True)
    unitMeasure = UnitMeasureModelSerializer(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'

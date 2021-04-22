# import Local Models
from erp_backend.products.models import Category

# import DRF
from rest_framework.serializers import ModelSerializer


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

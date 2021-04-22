# import Local Models
from erp_backend.products.models import UnitMeasure

# import DRF
from rest_framework.serializers import ModelSerializer


class UnitMeasureModelSerializer(ModelSerializer):
    class Meta:
        model = UnitMeasure
        fields = '__all__'

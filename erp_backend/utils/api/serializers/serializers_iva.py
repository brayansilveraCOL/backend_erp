# import Local Models
from erp_backend.utils.models import Iva

# import DRF
from rest_framework.serializers import ModelSerializer


class IvaModelSerializer(ModelSerializer):
    class Meta:
        model = Iva
        fields = '__all__'

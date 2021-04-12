# import Local Models
from erp_backend.utils.models import Parameter

# import DRF
from rest_framework.serializers import ModelSerializer


class ParameterModelSerializer(ModelSerializer):
    class Meta:
        model = Parameter
        fields = '__all__'

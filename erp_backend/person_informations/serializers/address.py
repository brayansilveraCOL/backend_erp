# Django models
from erp_backend.person_informations.models import Address
from erp_backend.users.models import User

# DRF
from rest_framework import serializers

# Serializers
from erp_backend.users.serializers.user import UserModelSerializer


class AddressModelSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter(is_active=True))

    class Meta:
        model = Address
        fields = '__all__'

    def create(self, data):
        address = Address.objects.create(**data)
        return address


class AddressDetailModelSerializer(serializers.ModelSerializer):
    user = UserModelSerializer(read_only=True)

    class Meta:
        model = Address
        fields = '__all__'


class AddressUpdateModelSerializer(serializers.ModelSerializer):
    address = serializers.CharField(max_length=25)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter(is_active=True))

    class Meta:
        model = Address
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.address = validated_data.get('address', instance.address)
        instance.save()
        return instance
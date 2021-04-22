# Django models
from django.core.validators import RegexValidator

from erp_backend.person_informations.models import Phone
from erp_backend.users.models import User

# DRF
from rest_framework import serializers

# Serializers
from erp_backend.users.serializers.user import UserModelSerializer


class PhoneModelSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter(is_active=True))

    class Meta:
        model = Phone
        fields = '__all__'

    def create(self, data):
        address = Phone.objects.create(**data)
        return address


class PhoneDetailModelSerializer(serializers.ModelSerializer):
    user = UserModelSerializer(read_only=True)

    class Meta:
        model = Phone
        fields = '__all__'


class PhoneUpdateModelSerializer(serializers.ModelSerializer):
    phone_regex = RegexValidator(regex=r'\+?1?\d{9,15}$',
                                 message="Not Valid Phone Number")
    phone_number = serializers.CharField(validators=[phone_regex], max_length=17)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter(is_active=True))

    class Meta:
        model = Phone
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.save()
        return instance

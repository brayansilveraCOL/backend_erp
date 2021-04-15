# Django models
from django.core.validators import RegexValidator

from erp_backend.person_informations.models import Contact
from erp_backend.users.models import User

# DRF
from rest_framework import serializers
# Serializers
from erp_backend.users.serializers.user import UserModelSerializer


class ContactModelSerializer(serializers.ModelSerializer):
    user = UserModelSerializer(read_only=True)

    class Meta:
        model = Contact
        fields = '__all__'


class ContactCreateSerializer(serializers.Serializer):
    address = serializers.CharField(max_length=25)
    full_name = serializers.CharField(max_length=50)
    phone_regex = RegexValidator(regex=r'\+?1?\d{9,15}$',
                                 message="Not Valid Phone Number")
    phone_number = serializers.CharField(validators=[phone_regex], max_length=17)
    title_contact = serializers.CharField(max_length=5)

    def create(self, data):
        user = self.context['user']
        contact = Contact.objects.create(user=user, **data)
        return contact

"""Users serializers."""

# Django
from django.contrib.auth import password_validation, authenticate
from django.core.validators import RegexValidator

# Django REST Framework
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator

# Models
from erp_backend.users.models import User
from erp_backend.person_informations.models import Phone, Address


class UserModelSerializer(serializers.ModelSerializer):
    """User model serializer."""

    class Meta:
        """Meta class."""

        model = User
        fields = ('username', 'first_name', 'last_name')


class UserLoginSerializer(serializers.Serializer):
    """User login serializer.

    Handle the login request data.
    """

    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, max_length=64)

    def validate(self, data):
        """Check credentials."""
        user = authenticate(username=data['email'], password=data['password'])
        if not user:
            raise serializers.ValidationError('Invalid credentials')
        self.context['user'] = user
        return data

    def create(self, data):
        """Generate or retrieve new token."""
        token, created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], token.key


class UserLogoutSerializer(serializers.Serializer):
    """ User Logout serializer.
    Handle the logout request data.
    """
    token = serializers.CharField(
        min_length=4,
        max_length=100,
    )

    def validate(self, data):
        token = Token.objects.filter(key=data['token'])
        if not token:
            raise serializers.ValidationError('token not exists')
        token.delete()
        return data


class UserSignUpSerializer(serializers.Serializer):
    """User sign up serializer.

    Handle sign up data validation and user/profile creation.
    """

    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        min_length=4,
        max_length=20,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    # Phone number
    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: +999999999. Up to 15 digits allowed."
    )
    phone_number = serializers.CharField(validators=[phone_regex], min_length=8, max_length=64)

    # Address
    address = serializers.CharField(min_length=8, max_length=64)

    # Type Identify
    typeIdentify = serializers.CharField(min_length=4, max_length=64)

    # identify
    identify = serializers.CharField(min_length=4, max_length=64,
                                     validators=[UniqueValidator(queryset=User.objects.all())]
                                     )

    # Password
    password = serializers.CharField(min_length=8, max_length=64)
    password_confirmation = serializers.CharField(min_length=8, max_length=64)

    # Name
    first_name = serializers.CharField(min_length=2, max_length=30)
    last_name = serializers.CharField(min_length=2, max_length=30)

    def validate(self, data):
        """Verify passwords match."""
        passwd = data['password']
        passwd_conf = data['password_confirmation']
        if passwd != passwd_conf:
            raise serializers.ValidationError("Passwords don't match.")
        password_validation.validate_password(passwd)
        return data

    def create(self, data):
        """Handle user and profile creation."""
        phone_number = data['phone_number']
        identify = data['identify']
        address = data['address']
        data.pop('password_confirmation')
        data.pop('phone_number')
        # data.pop('address')
        user = User.objects.create_user(**data)
        user.identify = identify
        user.save()
        Phone.objects.create(user=user, phone_number=phone_number)
        # phone.phone_number = data['phone_number']
        # phone.save()
        Address.objects.create(user=user, address=address)
        # address.address = address = data['address']
        # address.save()
        return user

    def update(self, instance, validated_data):
        pass

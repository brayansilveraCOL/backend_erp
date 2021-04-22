# Django Models
from erp_backend.users.models import User
from erp_backend.person_informations.models import Phone

# Serializer
from erp_backend.person_informations.serializers.phone import PhoneDetailModelSerializer, PhoneUpdateModelSerializer, PhoneModelSerializer

# rest-framework
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404


@api_view(['GET', 'POST'])
def phone_api_view(request, username=None):
    if username:
        users = User.objects.filter(username=username, is_active=True)
        if users:
            if request.method == 'GET':
                if users:
                    address_user_query = Phone.objects.filter(user=users[0], state=True)
                    if address_user_query:
                        serializer = PhoneModelSerializer(address_user_query, many=True)
                        return Response(serializer.data, status=status.HTTP_200_OK)
                    return Response(status=status.HTTP_400_BAD_REQUEST)
                return Response(status=status.HTTP_400_BAD_REQUEST)

            if request.method == 'POST':
                id_user = users.values('id')[0]['id']
                data = request.data
                data['user'] = id_user
                serializer = PhoneModelSerializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def phone_api_view_detail(request, username=None, uniqueCode=None):
    if request.method == 'GET':
        if username and uniqueCode:
            users = User.objects.filter(username=username, is_active=True)
            if users:
                phone = Phone.objects.filter(user=users[0], UniqueCode=uniqueCode, state=True)
                if phone:
                    serializer = PhoneDetailModelSerializer(phone, many=True)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                return Response(status=status.HTTP_400_BAD_REQUEST)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        if username and uniqueCode:
            users = User.objects.filter(username=username, is_active=True)
            if users:
                phone = Phone.objects.get(user=users[0], UniqueCode=uniqueCode, state=True)
                if phone:
                    id_user = users.values('id')[0]['id']
                    data = request.data
                    data['user'] = id_user
                    serializer = PhoneUpdateModelSerializer(phone, data=data)
                    serializer.is_valid(raise_exception=True)
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
                return Response(status=status.HTTP_400_BAD_REQUEST)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        if username and uniqueCode:
            users = User.objects.filter(username=username, is_active=True)
            if users:
                phone = Phone.objects.get(user=users[0], UniqueCode=uniqueCode, state=True)
                if phone:
                    phone.state = False
                    phone.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_400_BAD_REQUEST)





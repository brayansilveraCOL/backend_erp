# Django Models
from erp_backend.users.models import User
from erp_backend.person_informations.models import Address

# Serializer
from erp_backend.person_informations.serializers.address import AddressModelSerializer, AddressDetailModelSerializer, AddressUpdateModelSerializer

# rest-framework
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404


@api_view(['GET', 'POST'])
def address_api_view(request, username=None):
    if username:
        users = User.objects.filter(username=username, is_active=True)
        if users:
            if request.method == 'GET':
                if users:
                    address_user_query = Address.objects.filter(user=users[0], state=True)
                    if address_user_query:
                        serializer = AddressModelSerializer(address_user_query, many=True)
                        return Response(serializer.data, status=status.HTTP_200_OK)
                    return Response(status=status.HTTP_400_BAD_REQUEST)
                return Response(status=status.HTTP_400_BAD_REQUEST)

            if request.method == 'POST':
                id_user = users.values('id')[0]['id']
                data = request.data
                data['user'] = id_user
                serializer = AddressModelSerializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def address_api_view_detail(request, username=None, uniqueCode=None):
    if request.method == 'GET':
        if username and uniqueCode:
            users = User.objects.filter(username=username, is_active=True)
            if users:
                address = Address.objects.filter(user=users[0], UniqueCode=uniqueCode, state=True)
                if address:
                    serializer = AddressDetailModelSerializer(address, many=True)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                return Response(status=status.HTTP_400_BAD_REQUEST)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        if username and uniqueCode:
            users = User.objects.filter(username=username, is_active=True)
            if users:
                address = Address.objects.get(user=users[0], UniqueCode=uniqueCode, state=True)
                if address:
                    id_user = users.values('id')[0]['id']
                    data = request.data
                    data['user'] = id_user
                    serializer = AddressUpdateModelSerializer(address, data=data)
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
                address = Address.objects.get(user=users[0], UniqueCode=uniqueCode, state=True)
                if address:
                    address.state = False
                    address.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_400_BAD_REQUEST)





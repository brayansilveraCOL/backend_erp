# Models
from erp_backend.list_price.models import ListPrice, TypePlan, TypeSale

# Serializers
from erp_backend.list_price.api.serializers.listprice import ListCreatedSerializer, ListRetrieveAllModelSerializer, \
    ListPartialUpdateSerializer

# DRF
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def list_api_view(request):
    if request.method == 'POST':
        serializer = ListCreatedSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        list_price = serializer.save()
        serialize_price = ListRetrieveAllModelSerializer(list_price)
        return Response(serialize_price.data, status=status.HTTP_201_CREATED)
    elif request.method == 'GET':
        listPrice = ListPrice.objects.filter(state=True)
        serializer = ListRetrieveAllModelSerializer(listPrice, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'PATCH', 'DELETE'])
def detail_api_view(request, uniqueCode=None):
    if uniqueCode:
        list = ListPrice.objects.filter(state=True, UniqueCode=uniqueCode).first()
        if list:
            if request.method == 'PATCH':
                serializer = ListPartialUpdateSerializer(list, data=request.data, partial=True)
                serializer.is_valid(raise_exception=True)
                list_mod = serializer.save()
                serializer_return = ListRetrieveAllModelSerializer(list_mod)
                return Response(serializer_return.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_204_NO_CONTENT)

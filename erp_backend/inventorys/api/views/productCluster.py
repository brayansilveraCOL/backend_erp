# Models
from erp_backend.inventorys.cluster_model import ProductCluster

# Serializer
from erp_backend.inventorys.api.serializers.productCluster import ProductClusterCreateSerializer, \
    ProductClusterListModelSerializer, ProductClusterUpdatePartialSerializer

# DRF
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def api_view_product_cluster(request):
    if request.method == 'POST':
        serializer = ProductClusterCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        product_cluster_created = serializer.save()
        product_cluster_created = ProductClusterListModelSerializer(product_cluster_created)
        return Response(product_cluster_created.data, status=status.HTTP_201_CREATED)
    elif request.method == 'GET':
        product_cluster = ProductCluster.objects.filter(state=True)
        serializer = ProductClusterListModelSerializer(product_cluster, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'PATCH', 'DELETE'])
def api_detail_view_product_cluster(request, UniqueCode=None):
    if UniqueCode:
        product_cluster = ProductCluster.objects.filter(UniqueCode=UniqueCode, state=True).first()
        if product_cluster:
            if request.method == 'GET':
                serializer = ProductClusterListModelSerializer(product_cluster)
                return Response(serializer.data, status=status.HTTP_200_OK)
            elif request.method == 'PATCH':
                print(request.data)
                serializer = ProductClusterUpdatePartialSerializer(product_cluster, data=request.data, partial=True)
                serializer.is_valid(raise_exception=True)
                product_cluster_update = serializer.save()
                product_cluster_update = ProductClusterListModelSerializer(product_cluster_update)
                return Response(product_cluster_update.data, status=status.HTTP_202_ACCEPTED)
            elif request.method == 'DELETE':
                product_cluster.state = False
                product_cluster.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
            # elif request.method == 'POST':
            #     serializer = ProductClusterVerifyAmountSerializer(product_cluster, data=request.data, partial=True)
            #     serializer.is_valid(raise_exception=True)
            #     product_cluster_update = serializer.save()
            #     return Response(product_cluster_update.data, status=status.HTTP_202_ACCEPTED)
            else:
                return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_204_NO_CONTENT)


# Serializers
from erp_backend.products.api.serializers.product import ProductListModelSerializer
from erp_backend.inventorys.api.serializers.cluster import ClusterModelSerializer
from erp_backend.utils.api.serializers.serializers_iva import IvaModelSerializer
from erp_backend.users.serializers.user import UserModelSerializer

# Model
from erp_backend.inventorys.cluster_model import ProductCluster, Cluster
from erp_backend.products.models import Product
from erp_backend.utils.models import Iva
from erp_backend.users.models import User

# DRF
from rest_framework import serializers


class ProductClusterCreateSerializer(serializers.Serializer):
    cluster = serializers.PrimaryKeyRelatedField(queryset=Cluster.objects.filter(state=True))
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.filter(state=True))
    iva = serializers.PrimaryKeyRelatedField(queryset=Iva.objects.filter(state=True))
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter(is_active=True))
    quantity = serializers.IntegerField(min_value=0)
    status_cluster = serializers.CharField(max_length=150)
    minimum_quantity = serializers.IntegerField(min_value=0)
    observation = serializers.CharField(max_length=4000)
    purchase_price = serializers.DecimalField(max_digits=6, decimal_places=2)
    sale_price = serializers.DecimalField(max_digits=6, decimal_places=2)
    minimum_stock = serializers.BooleanField(default=False)

    def validate(self, attrs):
        """
        Validate
        :param attrs:
        :return: attrs
        """
        cluster = attrs['cluster']
        product = attrs['product']
        iva = attrs['iva']
        user = attrs['user']
        print(attrs['sale_price'])
        product_cluster = ProductCluster.objects.filter(cluster=cluster, product=product,
                                                        iva=iva, user=user, state=True)
        if product_cluster:
            raise serializers.ValidationError("Product In Cluster Active")

        return attrs

    def create(self, validated_data):
        return ProductCluster.objects.create(**validated_data)


class ProductClusterListModelSerializer(serializers.ModelSerializer):
    cluster = ClusterModelSerializer(read_only=True)
    product = ProductListModelSerializer(read_only=True)
    iva = IvaModelSerializer(read_only=True)
    user = UserModelSerializer(read_only=True)

    class Meta:
        model = ProductCluster
        fields = '__all__'


class ProductClusterUpdatePartialSerializer(serializers.Serializer):
    iva = serializers.PrimaryKeyRelatedField(queryset=Iva.objects.filter(state=True), required=False)
    status_cluster = serializers.CharField(max_length=150, required=False)
    observation = serializers.CharField(max_length=4000, required=False)
    purchase_price = serializers.DecimalField(max_digits=6, decimal_places=2, required=False)
    sale_price = serializers.DecimalField(max_digits=6, decimal_places=2, required=False)
    """
    Moment for develop, last delte this field
    """
    quantity = serializers.IntegerField(min_value=1)

    def validate(self, attrs):

        if attrs['status_cluster'] == 'LI' or attrs['status_cluster'] == 'SP':
            self.context['minimum_stock'] = True
        else:
            self.context['minimum_stock'] = False

        return attrs

    def update(self, instance, validated_data):

        instance.status_cluster = validated_data.get('status_cluster', instance.status_cluster)
        instance.observation = validated_data.get('observation', instance.observation)
        instance.purchase_price = validated_data.get('purchase_price', instance.purchase_price)
        instance.sale_price = validated_data.get('sale_price', instance.sale_price)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.minimum_stock = self.context['minimum_stock']
        instance.save()
        return instance


class ProductClusterUpdateQuantitySerializer(serializers.Serializer):
    quantity = serializers.IntegerField(min_value=1)
    minimum_stock = serializers.BooleanField(default=False)

    def update(self, instance, validated_data):
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.minimum_stock = validated_data.get('minimum_stock', instance.minimum_stock)
        instance.save()
        return instance





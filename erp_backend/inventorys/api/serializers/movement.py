# utils
from erp_backend.utils.functions.movement_internal_code import generate_code
# Models
from erp_backend.inventorys.cluster_model import ProductCluster, Cluster
from erp_backend.inventorys.type_movement_model import TypeMovement
from erp_backend.inventorys.models import Movement
from erp_backend.products.models import Product
from erp_backend.users.models import User

# Serializers
from erp_backend.users.serializers.user import UserModelSerializer
from erp_backend.inventorys.api.serializers.typeMovement import TypeMovementModelSerializer
from erp_backend.products.api.serializers.product import ProductListModelSerializer
from erp_backend.inventorys.api.serializers.cluster import ClusterModelSerializer
from erp_backend.inventorys.api.serializers.productCluster import ProductClusterListModelSerializer

# Rest Framework
from rest_framework import serializers


class MovementModelSerializer(serializers.ModelSerializer):
    """
    Serializer to LIst and Retrieve
    """
    typeMovement = TypeMovementModelSerializer(read_only=True)
    product = ProductListModelSerializer(read_only=True)
    user = UserModelSerializer(read_only=True)
    cluster = ClusterModelSerializer(read_only=True)
    productCluster = ProductClusterListModelSerializer(read_only=True)

    class Meta:
        model = Movement
        fields = '__all__'


class MovementCreateSerializer(serializers.Serializer):
    typeMovement = serializers.PrimaryKeyRelatedField(queryset=TypeMovement.objects.filter(state=True))
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.filter(state=True))
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter(is_active=True))
    observation = serializers.CharField(max_length=4000)
    quantity = serializers.IntegerField(min_value=1)
    status_movement = serializers.CharField(max_length=30)

    def validate(self, attrs):
        typeMovement = attrs['typeMovement']
        if typeMovement:
            if typeMovement.description == 'Entrada' or typeMovement.description == 'Retorno':
                self.context['operator'] = '+'
            else:
                self.context['operator'] = '-'
        else:
            raise serializers.ValidationError('Not Send Movement')

        product = attrs['product']
        if product:
            product_cluster = ProductCluster.objects.filter(state=True, product=product).first()
            if product_cluster:
                quantity = product_cluster.quantity
                quantity_request = attrs['quantity']
                if self.context['operator'] == '-':
                    if quantity_request > quantity:
                        raise serializers.ValidationError('The Quantity Exceed Value in Data Base please send value '
                                                          'less '
                                                          'than {}'.format(quantity - 10))
            else:
                raise serializers.ValidationError(
                    'Product not have in Product Cluster please verify in your Product Cluster Table')
        else:
            raise serializers.ValidationError('Not Send Product')
        user = attrs['user']
        if not user:
            raise serializers.ValidationError('Not Send User')
        if attrs['status_movement'] != 'AC' and attrs['status_movement'] != 'PR' and attrs['status_movement'] != 'CA':
            raise serializers.ValidationError(
                'Status Undefined {} you need send AC, PR, CA'.format(attrs['status_movement']))
        return attrs

    def create(self, validated_data):
        internal_code = generate_code()
        if self.context['operator'] == '+':
            product_cluster = ProductCluster.objects.filter(state=True, product=validated_data.get('product')).first()
            product_cluster.quantity = product_cluster.quantity + validated_data.get('quantity')
            product_cluster.minimum_stock = False
            product_cluster.save()
            return Movement.objects.create(InternalCode=internal_code,
                                           productCluster_id=product_cluster.pk,
                                           cluster_id=product_cluster.cluster.pk,
                                           **validated_data)


        else:
            pass

        pass


class MovementUpdateSerializer(serializers.Serializer):
    pass


class MovementReverseSerializer(serializers.Serializer):
    pass
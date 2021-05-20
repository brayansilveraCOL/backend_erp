# utils
import json
from erp_backend.utils.functions.movement_internal_code import generate_code
from erp_backend.utils.functions.create_json_dynamically import create_json_form
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
from erp_backend.inventorys.api.serializers.productCluster import ProductClusterListModelSerializer, \
    ProductClusterUpdateQuantitySerializer

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
    status_movement = serializers.CharField(max_length=30, default="AC")

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
        product_cluster = ProductCluster.objects.filter(state=True, product=validated_data.get('product')).first()
        if self.context['operator'] == '+':
            quantity = product_cluster.quantity + validated_data.get('quantity')
            minimum_stock = False
            """
            Values in order for Serializer
            """
            values = [quantity, minimum_stock]
            """
            call function create_json_form and i pass Serializer Instance and values array
            """
            jsonx = create_json_form(ProductClusterUpdateQuantitySerializer(), values)
            """
            return string and convert to json
            """
            json_form = json.loads(jsonx)
            """
            send to instance
            """
            update_quantity = ProductClusterUpdateQuantitySerializer(product_cluster, data=json_form)
            update_quantity.is_valid(raise_exception=True)
            update_quantity.save()
            return Movement.objects.create(InternalCode=internal_code,
                                           productCluster_id=product_cluster.pk,
                                           cluster_id=product_cluster.cluster.pk,
                                           **validated_data)
        elif self.context['operator'] == '-':
            if validated_data.get('quantity') < product_cluster.quantity:
                quantity = product_cluster.quantity - validated_data.get('quantity')
                execute = product_cluster.quantity - validated_data.get('quantity')
                minimum = product_cluster.minimum_quantity
                if execute > minimum:
                    minimum_stock = False
                    values = [quantity, minimum_stock]
                    json_generate = create_json_form(ProductClusterUpdateQuantitySerializer(), values)
                    json_form = json.loads(json_generate)
                    update_quantity = ProductClusterUpdateQuantitySerializer(product_cluster, data=json_form)
                    update_quantity.is_valid(raise_exception=True)
                    update_quantity.save()
                    return Movement.objects.create(InternalCode=internal_code,
                                                   productCluster_id=product_cluster.pk,
                                                   cluster_id=product_cluster.cluster.pk,
                                                   **validated_data)
                else:
                    minimum_stock = True
                    values = [quantity, minimum_stock]
                    json_generate = create_json_form(ProductClusterUpdateQuantitySerializer(), values)
                    json_form = json.loads(json_generate)
                    print(json_form)
                    update_quantity = ProductClusterUpdateQuantitySerializer(product_cluster, data=json_form)
                    update_quantity.is_valid(raise_exception=True)
                    update_quantity.save()
                    return Movement.objects.create(InternalCode=internal_code,
                                                   productCluster_id=product_cluster.pk,
                                                   cluster_id=product_cluster.cluster.pk,
                                                   **validated_data)
            else:
                raise serializers.ValidationError(
                    'the Quantity of the Request is greater than that of the inventory')
        else:
            raise serializers.ValidationError(
                'Operator not Defined {}'.format(self.context['operator']))
        pass


class MovementCancelSerializer(serializers.Serializer):
    uniqueCode = serializers.CharField(max_length=300)

    def update(self, instance, validated_data):
        movement = Movement.objects.filter(uniqueCode=validated_data.get('uniqueCode')).first()
        typeMovement = TypeMovement.objects.filter(pk=movement.typeMovement.pk).first()
        product_cluster = ProductCluster.objects.filter(product_id=movement.product.pk, state=True).first()
        quantity = product_cluster.quantity
        quantity_movement = movement.quantity
        if movement.status_movement != 'CA':
            if typeMovement.description == 'Entrada' or typeMovement.description == 'Retorno':
                result_quantity = quantity - quantity_movement
                if quantity_movement > quantity:
                    """
                    Condition pass test with this UUID 8a691fd57fed43c7a49948113f55de1f and modify productCluster a5351710976b4ba885bd0cca06d8a098
                    quantity 1
                    """
                    raise serializers.ValidationError(
                        'Dont Canceled this operation why movement quantity supered quantity Product Cluster please'
                        ' check and send request')
                else:
                    if result_quantity <= product_cluster.minimum_quantity:
                        """
                        Condition pass test with this UUID 8a691fd57fed43c7a49948113f55de1f at 90 and modify productCluster a5351710976b4ba885bd0cca06d8a098
                        quantity 100
                        """
                        minimum_stock = True
                        values = [result_quantity, minimum_stock]
                        json_generate = create_json_form(ProductClusterUpdateQuantitySerializer(), values)
                        json_form = json.loads(json_generate)
                        update_quantity = ProductClusterUpdateQuantitySerializer(product_cluster, data=json_form)
                        update_quantity.is_valid(raise_exception=True)
                        update_quantity.save()
                        instance.status_movement = 'CA'
                        instance.save()
                        return instance
                    else:
                        minimum_stock = False
                        values = [result_quantity, minimum_stock]
                        json_generate = create_json_form(ProductClusterUpdateQuantitySerializer(), values)
                        json_form = json.loads(json_generate)
                        update_quantity = ProductClusterUpdateQuantitySerializer(product_cluster, data=json_form)
                        update_quantity.is_valid(raise_exception=True)
                        update_quantity.save()
                        instance.status_movement = 'CA'
                        instance.save()
                        return instance

            elif typeMovement.description == 'Salida' or typeMovement.description == 'Devolucion':
                result_quantity = quantity + quantity_movement
                if result_quantity <= product_cluster.minimum_quantity:
                    """
                    Condition pass test with this UUID 90ab73fe5ba044449e5530f57d1a5322 and modify productCluster a5351710976b4ba885bd0cca06d8a098
                    quantity 1
                    """
                    minimum_stock = True
                    values = [result_quantity, minimum_stock]
                    json_generate = create_json_form(ProductClusterUpdateQuantitySerializer(), values)
                    json_form = json.loads(json_generate)
                    update_quantity = ProductClusterUpdateQuantitySerializer(product_cluster, data=json_form)
                    update_quantity.is_valid(raise_exception=True)
                    update_quantity.save()
                    instance.status_movement = 'CA'
                    instance.save()
                    return instance
                else:
                    """
                    Condition pass test with this UUID e6d59c0f7bb540b4a478dd020e86d349
                    """
                    minimum_stock = False
                    values = [result_quantity, minimum_stock]
                    json_generate = create_json_form(ProductClusterUpdateQuantitySerializer(), values)
                    json_form = json.loads(json_generate)
                    update_quantity = ProductClusterUpdateQuantitySerializer(product_cluster, data=json_form)
                    update_quantity.is_valid(raise_exception=True)
                    update_quantity.save()
                    instance.status_movement = 'CA'
                    instance.save()
                    return instance
        else:
            raise serializers.ValidationError('can not cancelled one movement  that  status now is cancelled please '
                                              'contact the administrator')

        return instance


class MovementUpdateStatus(serializers.Serializer):
    """
    This class serializer change status different to cancelled
    """
    pass

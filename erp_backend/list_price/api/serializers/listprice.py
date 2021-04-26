# Model
from erp_backend.list_price.models import ListPrice, TypeSale, TypePlan
from erp_backend.products.models import Product

# DRF
from rest_framework import serializers

# Serializers

from erp_backend.products.api.serializers.product import ProductModelSerializer
from erp_backend.list_price.api.serializers.typesale import TypeSaleModelSerializer
from erp_backend.list_price.api.serializers.typeplan import TypePlanModelSerializer


class ListCreatedSerializer(serializers.Serializer):
    typeSale = serializers.PrimaryKeyRelatedField(queryset=TypeSale.objects.filter(state=True))
    typePlan = serializers.PrimaryKeyRelatedField(queryset=TypePlan.objects.filter(state=True))
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.filter(state=True))
    fullPrice = serializers.DecimalField(max_digits=6, decimal_places=2)

    def validate(self, attrs):
        typeSale = attrs['typeSale']
        typePlan = attrs['typePlan']
        product = attrs['product']

        list_price_created = ListPrice.objects.filter(typePlan=typePlan,
                                                      typeSale=typeSale,
                                                      product=product,
                                                      state=True)
        if list_price_created:
            raise serializers.ValidationError("List Price its already Created")
        return attrs

    def create(self, validated_data):
        typeSale = validated_data['typeSale']
        ts = TypeSale.objects.filter(description=typeSale, state=True)
        if ts.values('description')[0]['description'] == 'Contado':
            plan = TypePlan.objects.filter(description='Plan 0', state=True)
            id_plan = plan.values('id')[0]['id']
            validated_data.pop('typePlan')
            list_price_created = ListPrice.objects.filter(typePlan_id=id_plan,
                                                          typeSale=validated_data['typeSale'],
                                                          product=validated_data['product'],
                                                          state=True)
            if list_price_created:
                raise serializers.ValidationError("List Price its already Created")
            list = ListPrice.objects.create(typePlan_id=id_plan, **validated_data)
            return list
        list_cred = ListPrice.objects.create(**validated_data)
        return list_cred


class ListRetrieveAllModelSerializer(serializers.ModelSerializer):
    typeSale = TypeSaleModelSerializer(read_only=True)
    typePlan = TypePlanModelSerializer(read_only=True)
    product = ProductModelSerializer(read_only=True)

    class Meta:
        model = ListPrice
        fields = '__all__'


class ListPartialUpdateSerializer(serializers.Serializer):
    fullPrice = serializers.DecimalField(max_digits=6, decimal_places=2)

    def update(self, instance, validated_data):
        print(validated_data.get('fullPrice'))
        instance.fullPrice = validated_data.get('fullPrice', instance.fullPrice)
        instance.save()
        return instance

# Import Local Models
from erp_backend.products.models import Product, Category, UnitMeasure

# Import Serializers
from erp_backend.products.api.serializers.product import ProductModelSerializer, ProductListModelSerializer
# Import DRF
from rest_framework import mixins, viewsets, response, status

# Permission
from rest_framework.permissions import IsAdminUser


class ProductViewSet(mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
    serializer_class = ProductModelSerializer
    queryset = Product.objects.filter(state=True)
    lookup_field = 'UniqueCode'

    def get_permissions(self):
        """Assign permissions based on action."""
        permissions = [IsAdminUser]
        return [permission() for permission in permissions]

    def perform_destroy(self, instance):
        """Disable Iva."""
        instance.state = False
        instance.save()

    def create(self, request, *args, **kwargs):
        print(request.data)
        data_request = request.data
        id_category = data_request['category']
        id_unit_measure = data_request['unitMeasure']
        category = Category.objects.filter(id=id_category)
        unitMeasure = UnitMeasure.objects.filter(id=id_unit_measure)
        data_request['category_id'] = category.values('id')[0]['id']
        data_request['unitMeasure_id'] = unitMeasure.values('id')[0]['id']
        serializer = ProductModelSerializer(data=data_request)
        serializer.is_valid(raise_exception=True)
        product = serializer.save()
        serializers = ProductListModelSerializer(product)
        return response.Response(serializers.data, status=status.HTTP_201_CREATED)


class ProductListViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet):
    serializer_class = ProductListModelSerializer
    queryset = Product.objects.filter(state=True)
    lookup_field = 'UniqueCode'

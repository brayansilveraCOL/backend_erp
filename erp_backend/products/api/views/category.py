# Import Local Models
from erp_backend.products.models import Category

# Import Serializers
from erp_backend.products.api.serializers.category import CategoryModelSerializer
# Import DRF
from rest_framework import mixins, viewsets

# Permission
from rest_framework.permissions import IsAdminUser


class CategoryViewSet(mixins.CreateModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.ListModelMixin,
                         mixins.DestroyModelMixin,
                         viewsets.GenericViewSet):
    serializer_class = CategoryModelSerializer
    queryset = Category.objects.filter(state=True)
    lookup_field = 'UniqueCode'

    def get_permissions(self):
        """Assign permissions based on action."""
        permissions = [IsAdminUser]
        return [permission() for permission in permissions]

    def perform_destroy(self, instance):
        """Disable Iva."""
        instance.state = False
        instance.save()

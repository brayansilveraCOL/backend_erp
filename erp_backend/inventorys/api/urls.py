# Django
from django.urls import include, path, re_path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views.typeMovement import TypeMovementViewSet
from .views.cluster import ClusterViewSet
from .views.productCluster import api_view_product_cluster, api_detail_view_product_cluster

router = DefaultRouter()
router.register(r'typeMovement', TypeMovementViewSet, basename='typeMovement'),
router.register(r'cluster', ClusterViewSet, basename='cluster'),

urlpatterns = [
    path('', include(router.urls)),
    path('cluster/product', api_view_product_cluster, name='cluster-product'),
    re_path(r'cluster/product/(?P<UniqueCode>[-a-zA-Z0-9_]+)',
            api_detail_view_product_cluster, name='cluster-product-detail')

]

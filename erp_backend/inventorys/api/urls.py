# Django
from django.urls import include, path, re_path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views.typeMovement import TypeMovementViewSet
from .views.cluster import ClusterViewSet
from .views.movement import ListRetrieveMovementViewSet, api_view_movement
from .views.productCluster import api_view_product_cluster, api_detail_view_product_cluster
from .views.movement import api_view_detail_movement

router = DefaultRouter()
router.register(r'typeMovement', TypeMovementViewSet, basename='typeMovement'),
router.register(r'cluster', ClusterViewSet, basename='cluster'),
router.register(r'movement', ListRetrieveMovementViewSet, basename='movement'),



urlpatterns = [
    path('', include(router.urls)),
    path('cluster/product', api_view_product_cluster, name='cluster-product'),
    path('movement/product', api_view_movement, name='cluster-product-movement'),
    re_path(r'cluster/product/(?P<UniqueCode>[-a-zA-Z0-9_]+)',
            api_detail_view_product_cluster, name='cluster-product-detail'),
    re_path(r'movement/product/(?P<UniqueCode>[-a-zA-Z0-9_]+)',
            api_view_detail_movement, name='cluster-product-detail')

    # re_path(r'cluster/product/(?P<UniqueCode>[-a-zA-Z0-9_]+)/quantity',
    #         api_detail_view_product_cluster, name='cluster-product-quantity-detail')

]

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views.unitmeasure import UnitMeasureViewSet
from .views.category import CategoryViewSet
from .views.product import ProductViewSet, ProductListViewSet

router = DefaultRouter()
router.register(r'unit', UnitMeasureViewSet, basename='unitMeasure'),
router.register(r'category', CategoryViewSet, basename='category'),
router.register(r'product', ProductViewSet, basename='product'),
router.register(r'products', ProductListViewSet, basename='products'),


urlpatterns = [
    path('', include(router.urls))
]

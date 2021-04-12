# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views.api_iva import IvaViewSet
from .views.api_parameter import ParameterViewSet

router = DefaultRouter()
router.register(r'iva', IvaViewSet, basename='iva')
router.register(r'parameter', ParameterViewSet, basename='iva')

urlpatterns = [
    path('', include(router.urls))
]
# Django
from django.urls import include, path, re_path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views.typeplan import TypePlanViewSet
from .views.typesale import TypeSaleViewSet
from .views.listprice import list_api_view, detail_api_view

router = DefaultRouter()
router.register(r'plan', TypePlanViewSet, basename='plan'),
router.register(r'sale', TypeSaleViewSet, basename='sale'),

urlpatterns = [
    path('', include(router.urls)),
    path('list/', list_api_view, name='list'),
    re_path(r'list/(?P<uniqueCode>[-a-zA-Z0-9_]+)', detail_api_view, name='list-detail')

]

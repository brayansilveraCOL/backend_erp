"""Person Information URLs."""

# Django
from django.urls import include, path, re_path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from erp_backend.person_informations.views import ContactViewSet, ContactDetailViewSet
from erp_backend.person_informations.views.address import address_api_view, address_api_view_detail

router = DefaultRouter()
router.register(
    r'users/(?P<username>[-a-zA-Z0-9_]+)/contact',
    ContactDetailViewSet,
    basename='contacts-unique'
)
router.register(
    r'users/(?P<username>[-a-zA-Z0-9_]+)/contacts',
    ContactViewSet,
    basename='contacts'
)
urlpatterns = [
    path('', include(router.urls)),
    re_path(r'users/(?P<username>[-a-zA-Z0-9_]+)/addresses', address_api_view, name='addresses'),
    re_path(r'user/(?P<username>[-a-zA-Z0-9_]+)/address/(?P<uniqueCode>[-a-zA-Z0-9_]+)',
            address_api_view_detail, name='addresses-detail')

]

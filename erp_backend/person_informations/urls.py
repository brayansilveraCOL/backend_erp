"""Person Information URLs."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from erp_backend.person_informations.views import ContactViewSet, ContactDetailViewSet

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
    path('', include(router.urls))
]

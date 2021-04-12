"""Utils permission classes."""

# Django REST Framework
from rest_framework.permissions import BasePermission

# Models
from erp_backend.users.models import User


class IsAdminPlatform(BasePermission):
    """Allow access only to admins."""

    def has_object_permission(self, request, view, obj):
        """Verify user have a membership in the obj."""
        try:
            User.objects.get(
                pk=request.pk,
                username=request.username,
                is_staff=True
            )
        except User.DoesNotExist:
            return False
        return True

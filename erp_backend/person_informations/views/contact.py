# Serializer
from erp_backend.person_informations.serializers.contact import ContactModelSerializer, ContactCreateSerializer

# Models
from erp_backend.person_informations.models import Contact
from erp_backend.users.models import User

# DRF
from rest_framework import viewsets, status
from rest_framework.viewsets import mixins
from rest_framework.generics import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response

# Django
from rest_framework.permissions import IsAdminUser, IsAuthenticated


class ContactViewSet(mixins.ListModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.CreateModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
    serializer_class = ContactModelSerializer

    def dispatch(self, request, *args, **kwargs):
        username = kwargs['username']
        users = User.objects.filter(username=username, is_active=True)
        self.user = get_object_or_404(users)
        return super(ContactViewSet, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        """Return circle members."""
        return Contact.objects.filter(
            user=self.user,
            state=True
        )

    def get_permissions(self):
        permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        serializer = ContactCreateSerializer(data=request.data,
                                             context={'user': self.user})
        serializer.is_valid(raise_exception=True)
        contact = serializer.save()
        data = self.get_serializer(contact).data
        return Response(data, status=status.HTTP_201_CREATED)

    def partial_update(self, request, *args, **kwargs):
        pass


class ContactDetailViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet):
    serializer_class = ContactModelSerializer
    lookup_field = 'UniqueCode'
    queryset = Contact.objects.filter(state=True)

    def get_permissions(self):
        """Assign permissions based on action."""
        permissions = [IsAdminUser]
        return [permission() for permission in permissions]

    def perform_destroy(self, instance):
        """Disable Iva."""
        instance.state = False
        instance.save()
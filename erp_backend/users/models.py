from django.db import models
from django.contrib.auth.models import AbstractUser
from simple_history.models import HistoricalRecords
from django.utils.translation import gettext_lazy as _
from erp_backend.utils.choices.choices import TYPE_IDENTIFY


class User(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField('Email', max_length=255, unique=True)
    first_name = models.CharField('First Name', max_length=255, blank=True, null=True)
    last_name = models.CharField('Last Name', max_length=255, blank=True, null=True)
    image = models.ImageField('Photo', upload_to='perfil/', max_length=255, null=True, blank=True)
    code_provider = models.CharField(_('Provider Code'), blank=True, null=True, max_length=17)
    identify = models.CharField(_('Identify User'), null=True, blank=True, unique=True, max_length=17)
    title_user = models.CharField(_('User Contact'), blank=True, null=True, max_length=5)
    is_active = models.BooleanField(default=True)
    is_client = models.BooleanField(
        _('client status'),
        default=True,
        help_text=_('Help to perform Query.'
                    'Clients are the main type user'),
    )
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Help to perform query.'
                    'Staff are the main type user'),
    )
    is_provider = models.BooleanField(
        _('provider status'),
        default=False,
        help_text=_('Help to perform query.'
                    'Provider are the main type user'),
    )
    typeIdentify = models.CharField('Type Identify', max_length=100, choices=TYPE_IDENTIFY, null=True)
    historical = HistoricalRecords()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username

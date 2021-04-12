from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
# Utils Import
from erp_backend.AbstractClasses.BaseModel import BaseModel
from erp_backend.users.models import User
# THIRD_PARTY Imports
from simple_history.models import HistoricalRecords


class Phone(BaseModel):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    phone_regex = RegexValidator(regex=r'\+?1?\d{9,15}$',
                                 message="Not Valid Phone Number")
    phone_number = models.CharField(_('Phone Number'), blank=True, null=True, validators=[phone_regex], max_length=17)
    Historical = HistoricalRecords()

    def __str__(self):
        """

        :return: Phone representation
        """
        return self.phone_number

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value


class Address(BaseModel):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    address = models.CharField(_('Address User'), blank=True, null=True, max_length=25)
    Historical = HistoricalRecords()

    def __str__(self):
        """

        :return: address representation
        """
        return self.address

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value


class Contact(BaseModel):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    address = models.CharField(_('Address User'), blank=True, null=True, max_length=25)
    full_name = models.CharField(_('Full Name Contact'), blank=True, null=True, max_length=50)
    phone_regex = RegexValidator(regex=r'\+?1?\d{9,15}$',
                                 message="Not Valid Phone Number")
    phone_number = models.CharField(_('Phone Number'), blank=True, null=True, validators=[phone_regex], max_length=17)
    title_contact = models.CharField(_('Title Contact'), blank=True, null=True, max_length=5)
    Historical = HistoricalRecords()

    def __str__(self):
        """

        :return: Contact representation
        """
        return str(self.full_name)

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value
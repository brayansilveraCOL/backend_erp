"""
User Generic classes Type Identification, Phone Users, Address User, Contacts User
and this class inherits  the utils class and Users inherits this class
"""

# Django import
from django.db import models
from django.utils.translation import gettext_lazy as _

# django thirdParty Imports
from simple_history.models import HistoricalRecords

# Model Custom Imports
from erp_backend.AbstractClasses.BaseModel import BaseModel


class TypeIdentification(BaseModel):
    description = models.CharField(_('Description Type Identification'), blank=False, null=False, unique=True,
                                   max_length=40)
    Historical = HistoricalRecords()

    def __str__(self):
        """

        :return: description representation
        """
        return str(self.description)

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

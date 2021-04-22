import uuid

from django.db import models

# Local imports
from erp_backend.AbstractClasses.BaseModel import BaseModel

# Third Party Model
from simple_history.models import HistoricalRecords


# Create your models here.


class UnitMeasure(BaseModel):
    UniqueCode = models.UUIDField('Code Unique Generate', default=uuid.uuid4, editable=False)
    description = models.CharField('Unit Measure', max_length=100, unique=True, blank=False, null=False)
    historical = HistoricalRecords()

    def __str__(self):
        return self.description

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value


class Category(BaseModel):
    UniqueCode = models.UUIDField('Code Unique Generate', default=uuid.uuid4, editable=False)
    description = models.CharField('Category Product', max_length=100, unique=True, blank=False, null=False)
    historical = HistoricalRecords()

    def __str__(self):
        return self.description

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value


class Product(BaseModel):
    UniqueCode = models.UUIDField('Code Unique Generate', default=uuid.uuid4, editable=False)
    name = models.CharField('Name Product', max_length=255, unique=True, blank=False, null=False)
    description = models.CharField('Description Product', max_length=500, blank=True, null=True)
    unitPrice = models.DecimalField('unity Price For Product', max_digits=6, decimal_places=2)
    unitMeasure = models.ForeignKey(UnitMeasure, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    historical = HistoricalRecords()

    def __str__(self):
        return self.name

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

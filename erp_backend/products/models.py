from django.db import models

# Local imports
from erp_backend.AbstractClasses.BaseModel import BaseModel

# Third Party Model
from simple_history.models import HistoricalRecords


# Create your models here.


class UnitMeasure(BaseModel):
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
    name = models.CharField('Name Product', max_length=255, unique=True, blank=False, null=False)
    description = models.CharField('Description Product', max_length=500, blank=True, null=True)
    unitPrice = models.DecimalField('unity Price For Product', max_digits=6, decimal_places=2)
    unitMeasure = models.ForeignKey(UnitMeasure, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    historical = HistoricalRecords()

    def __str__(self):
        return self.name

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

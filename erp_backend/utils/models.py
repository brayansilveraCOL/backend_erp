from django.db import models
# Local imports
from erp_backend.AbstractClasses.BaseModel import BaseModel
# Third Party Model
from simple_history.models import HistoricalRecords


class Iva(BaseModel):
    ano = models.PositiveIntegerField('Iva', unique=True, blank=False, null=False)
    percent = models.PositiveIntegerField('Percent Iva')
    historical = HistoricalRecords()

    def __str__(self):
        return self.ano

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value


class Parameter(BaseModel):
    value = models.CharField(max_length=100)
    historical = HistoricalRecords()

    def __str__(self):
        return self.value

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

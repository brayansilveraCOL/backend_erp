from django.db import models
# Local imports
from erp_backend.AbstractClasses.BaseModel import BaseModel

# Third Party Model
from simple_history.models import HistoricalRecords


class TypeMovement(BaseModel):
    description = models.CharField('Type  Movement', max_length=100, unique=True, blank=False, null=False)
    historical = HistoricalRecords()

    def __str__(self):
        return self.description

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

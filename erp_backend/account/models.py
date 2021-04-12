# Imports Pyhton
import uuid

from django.db import models
# Local imports
from erp_backend.AbstractClasses.BaseModel import BaseModel
from erp_backend.users.models import User
from erp_backend.billing.models import Bill
from erp_backend.list_price.models import TypePlan
from erp_backend.utils.choices.choices import STATUS_ACCOUNT
# Third Party Model
from simple_history.models import HistoricalRecords


class Account(BaseModel):
    UniqueCode = models.UUIDField('Code Unique Generate', default=uuid.uuid4, editable=False)
    CodeInternal = models.CharField('Code Unique Internal', max_length=10, unique=True, null=False, blank=False)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer')
    userInternal = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_internal')
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    quotas = models.ForeignKey(TypePlan, on_delete=models.CASCADE, verbose_name='Number of Quotas Plan')
    date_payment_initial = models.DateField('Date Payment Initial')
    date_payment_final = models.DateField('Date Payment Final')
    average_pay_rate = models.DecimalField('Average Pay Rate', max_digits=6, decimal_places=2,
                                           help_text='Average Pay Rate')
    balance_due = models.DecimalField('Balance Due', max_digits=6, decimal_places=2,
                                      help_text='Balance Due Account', null=True)
    status_account_internal = models.CharField(max_length=50, choices=STATUS_ACCOUNT, verbose_name='Status account')

    historical = HistoricalRecords()

    def __str__(self):
        return self.CodeInternal

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

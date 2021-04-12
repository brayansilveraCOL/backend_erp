# Imports Pyhton
import uuid

from django.db import models
# Local imports
from erp_backend.AbstractClasses.BaseModel import BaseModel
from erp_backend.users.models import User
from erp_backend.billing.models import Bill
from erp_backend.account.models import Account
from erp_backend.utils.choices.choices import STATUS_PAYMENT
# Third Party Model
from simple_history.models import HistoricalRecords


class TypePayment(BaseModel):
    description = models.CharField('Type Payment', max_length=100, unique=True, blank=False, null=False)
    historical = HistoricalRecords()

    def __str__(self):
        return self.description

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value


class Payment(BaseModel):
    UniqueCode = models.UUIDField('Code Unique Generate', default=uuid.uuid4, editable=False)
    CodeInternal = models.CharField('Code Unique Internal', max_length=10, unique=True, null=False, blank=False)
    userInternal = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payment_internal')
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payment_customer')
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    typePayment = models.ForeignKey(TypePayment, on_delete=models.CASCADE)
    quota_ammount = models.DecimalField('Pay', max_digits=6, decimal_places=2,
                                        help_text='Pay')
    quota = models.PositiveIntegerField(verbose_name='Quota Payment')
    status_payment_internal = models.CharField(max_length=50, choices=STATUS_PAYMENT, verbose_name='Status Payment')
    date_payment_initial = models.DateField('Date Payment Initial')
    date_payment_final = models.DateField('Date Payment Final')

    historical = HistoricalRecords()

    def __str__(self):
        return self.account.CodeInternal

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

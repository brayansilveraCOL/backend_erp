# Imports Pyhton
import uuid

from django.db import models
# Local imports
from erp_backend.AbstractClasses.BaseModel import BaseModel
from erp_backend.list_price.models import TypePlan, TypeSale, ListPrice
from erp_backend.users.models import User
from erp_backend.utils.choices.choices import STATUS_BILL
from erp_backend.products.models import Product
from erp_backend.utils.models import Iva
# Third Party Model
from simple_history.models import HistoricalRecords


class Bill(BaseModel):
    UniqueCode = models.UUIDField('Code Unique Generate', default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    typePlan = models.ForeignKey(TypePlan, on_delete=models.CASCADE)
    typeSale = models.ForeignKey(TypeSale, on_delete=models.CASCADE)
    CodeInternal = models.CharField('Code Unique Internal', max_length=10, unique=True, null=False, blank=False)
    billing_cut = models.CharField('Date of the month where payment Bill', max_length=15, null=False, blank=False)
    billing_status = models.CharField(max_length=50, choices=STATUS_BILL, blank=False, null=False)
    total_charged = models.DecimalField('Total Charged', max_digits=6, decimal_places=2,
                                        help_text='This Field Total Charged'
                                                  'Products')
    historical = HistoricalRecords()

    def __str__(self):
        return self.CodeInternal

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value


class BillDetail(BaseModel):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    listPrice = models.ForeignKey(ListPrice, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField('Quantity Product')
    total = models.DecimalField('Total Product', max_digits=6, decimal_places=2)
    iva = models.ForeignKey(Iva, on_delete=models.CASCADE)

    historical = HistoricalRecords()

    def __str__(self):
        return self.bill.CodeInternal

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

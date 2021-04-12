from django.db import models

# Local imports
from erp_backend.AbstractClasses.BaseModel import BaseModel
from erp_backend.products.models import Category, Product

# Third Party Model
from simple_history.models import HistoricalRecords


class TypeDiscount(BaseModel):
    description = models.CharField('Type  Discount', max_length=100, unique=True, blank=False, null=False)
    historical = HistoricalRecords()

    def __str__(self):
        return self.description

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value


class DiscountCategory(BaseModel):
    typeDiscount = models.ForeignKey(TypeDiscount, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    percent = models.PositiveIntegerField('Percent Discount')
    historical = HistoricalRecords()

    def __str__(self):
        return self.Category.description

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value


class DiscountProduct(BaseModel):
    typeDiscount = models.ForeignKey(TypeDiscount, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    percent = models.PositiveIntegerField('Percent Discount')
    historical = HistoricalRecords()

    def __str__(self):
        return self.Product.name

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

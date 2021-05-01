import uuid

from django.db import models

# Local imports
from erp_backend.AbstractClasses.BaseModel import BaseModel
from erp_backend.products.models import Product

# Third Party Model
from simple_history.models import HistoricalRecords


class TypePlan(BaseModel):
    UniqueCode = models.UUIDField('Code Unique Generate', default=uuid.uuid4, editable=False)
    description = models.CharField('Type  Plan', max_length=100, unique=True, blank=False, null=False)
    quota = models.PositiveIntegerField('Quota Plan')
    historical = HistoricalRecords()

    def __str__(self):
        return self.description

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value


class TypeSale(BaseModel):
    UniqueCode = models.UUIDField('Code Unique Generate', default=uuid.uuid4, editable=False)
    description = models.CharField('Type  Sale', max_length=100, unique=True, blank=False, null=False)
    historical = HistoricalRecords()

    def __str__(self):
        return self.description

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value


class ListPrice(BaseModel):
    UniqueCode = models.UUIDField('Code Unique Generate', default=uuid.uuid4, editable=False)
    typeSale = models.ForeignKey(TypeSale, on_delete=models.CASCADE)
    typePlan = models.ForeignKey(TypePlan, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    fullPrice = models.DecimalField('unity Price For Product', max_digits=6, decimal_places=2)# Get Full Price in
    # Product Cluster
    historical = HistoricalRecords()



    def __str__(self):
        return self.product.name

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

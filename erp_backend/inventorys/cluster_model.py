import uuid

from django.db import models
# Local imports
from erp_backend.AbstractClasses.BaseModel import BaseModel
from erp_backend.products.models import Product
from erp_backend.users.models import User
from erp_backend.utils.models import Iva
from erp_backend.utils.choices.choices import STATUS_CLUSTER
# Third Party Model
from simple_history.models import HistoricalRecords


class Cluster(BaseModel):
    UniqueCode = models.UUIDField('Code Unique Generate', default=uuid.uuid4, editable=False)
    name = models.CharField('Name Cluster', max_length=100, unique=True, blank=False, null=False)
    historical = HistoricalRecords()

    def __str__(self):
        return self.name

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value


class ProductCluster(BaseModel):
    UniqueCode = models.UUIDField('Code Unique Generate', default=uuid.uuid4, editable=False)
    cluster = models.ForeignKey(Cluster, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    iva = models.ForeignKey(Iva, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField('Quantity Product')
    status_cluster = models.CharField('Status Product in Cluster', max_length=150, choices=STATUS_CLUSTER)
    minimum_quantity = models.PositiveSmallIntegerField('Minimum Quantity Product')
    observation = models.CharField('Observation Cluster Stock', max_length=4000)
    purchase_price = models.DecimalField('Purchase Price Product in Cluster', max_digits=6, decimal_places=2,
                                         help_text='This Field Purchase Price'
                                                   'Product')
    sale_price = models.DecimalField('Purchase Price Product in Cluster', max_digits=6, decimal_places=2,
                                     help_text='This Field Sale Price'
                                               'Product')
    minimum_stock = models.BooleanField('Minimum Stock', default=False, help_text='this Field alarm, This product is '
                                                                                  'out of stock ')
    historical = HistoricalRecords()

    def __str__(self):
        return self.cluster.name

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

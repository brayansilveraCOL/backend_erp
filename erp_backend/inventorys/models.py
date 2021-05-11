# Imports Pyhton
import uuid

from django.db import models
# Local imports
from erp_backend.AbstractClasses.BaseModel import BaseModel
from erp_backend.products.models import Product
from erp_backend.users.models import User
from erp_backend.inventorys.cluster_model import Cluster
from erp_backend.inventorys.type_movement_model import TypeMovement
from erp_backend.inventorys.cluster_model import ProductCluster
from erp_backend.utils.choices.choices import STATUS_MOVEMENT
# Third Party Model
from simple_history.models import HistoricalRecords


class Movement(BaseModel):
    InternalCode = models.CharField('Code internal', unique=True, max_length=50)
    uniqueCode = models.UUIDField('Code Unique Generate', default=uuid.uuid4, editable=False)
    typeMovement = models.ForeignKey(TypeMovement, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cluster = models.ForeignKey(Cluster, on_delete=models.CASCADE)
    productCluster = models.ForeignKey(ProductCluster, on_delete=models.CASCADE)
    observation = models.CharField('Observation Cluster Movement', max_length=4000)
    quantity = models.PositiveSmallIntegerField('Quantity Product')
    status_movement = models.CharField('Status Movement', max_length=30, choices=STATUS_MOVEMENT)
    historical = HistoricalRecords()

    def __str__(self):
        return self.InternalCode

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

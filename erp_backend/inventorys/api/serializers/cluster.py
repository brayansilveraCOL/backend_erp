# Model
from erp_backend.inventorys.cluster_model import Cluster

# DRF
from rest_framework import serializers


class ClusterModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cluster
        fields = '__all__'

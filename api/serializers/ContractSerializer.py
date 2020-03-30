from rest_framework import serializers
from ..models.ContractModel import Contract

class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'
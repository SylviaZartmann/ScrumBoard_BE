from rest_framework import serializers
from contracts.models import Contract

class ContractSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contract
        fields = ['number', 'contracting_date', 'contracting_kind', 'order_value', 'contractor', 'client', 'date_start', 'date_end', 'precessing_time']
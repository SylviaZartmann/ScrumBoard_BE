from django.shortcuts import render
from rest_framework import viewsets

from contracts.models import Contract
from contracts.serializers import ContractSerializer

# Create your views here.
class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
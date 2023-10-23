from django.shortcuts import render
from rest_framework import viewsets

from employees.models import Employee
from employees.serializers import EmployeeSerializer

# ViewSets define the view behavior.
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all().order_by('lastname')
    serializer_class = EmployeeSerializer
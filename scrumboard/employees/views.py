from django.shortcuts import render
from rest_framework import viewsets

from employees.models import Employee
from employees.serializers import EmployeeSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

# ViewSets define the view behavior.
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
    
    
    
    
    
    
    
    
    
    # @csrf_exempt
    # def employee_list(request):
    #     if request.method == 'GET':
    #         queryset = Employee.objects.all().order_by('lastname')
    #         serializer = EmployeeSerializer(queryset, many=True)
    #         return JsonResponse(serializer.data, safe=False)
        
    #     elif request.method == 'POST':
    #         data = JSONParser().parse(request)
    #         serializer = EmployeeSerializer(data=data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return JsonResponse(serializer.data, status=201)
    #         return JsonResponse(serializer.errors, status=400)
    
    # def employee_detail(request, pk):
    #     try:
    #         queryset = Employee.objects.get(pk=pk)
    #     except Employee.DoesNotExist:
    #         return HttpResponse(status=404)

    #     if request.method == 'GET':
    #         serializer = EmployeeSerializer(queryset)
    #         return JsonResponse(serializer.data)

    #     elif request.method == 'PUT':
    #         data = JSONParser().parse(request)
    #         serializer = EmployeeSerializer(queryset, data=data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return JsonResponse(serializer.data)
    #         return JsonResponse(serializer.errors, status=400)

    #     elif request.method == 'DELETE':
    #         queryset.delete()
    #         return HttpResponse(status=204)
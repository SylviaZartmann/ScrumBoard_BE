from django.shortcuts import render
from rest_framework import viewsets

from contracts.models import Contract
from contracts.serializers import ContractSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    
    
    
    
    
    
    
    
    
    
    
    # @csrf_exempt
    # def contract_list(request):
    #     if request.method == 'GET':
    #         queryset = Contract.objects.all()
    #         serializer = ContractSerializer(queryset, many=True)
    #         return JsonResponse(serializer.data, safe=False)
        
    #     elif request.method == 'POST':
    #         data = JSONParser().parse(request)
    #         serializer = ContractSerializer(data=data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return JsonResponse(serializer.data, status=201)
    #         return JsonResponse(serializer.errors, status=400)
    
    # def client_detail(request, pk):
    #     try:
    #         queryset = Contract.objects.get(pk=pk)
    #     except Contract.DoesNotExist:
    #         return HttpResponse(status=404)

    #     if request.method == 'GET':
    #         serializer = ContractSerializer(queryset)
    #         return JsonResponse(serializer.data)

    #     elif request.method == 'PUT':
    #         data = JSONParser().parse(request)
    #         serializer = ContractSerializer(queryset, data=data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return JsonResponse(serializer.data)
    #         return JsonResponse(serializer.errors, status=400)

    #     elif request.method == 'DELETE':
    #         queryset.delete()
    #         return HttpResponse(status=204)
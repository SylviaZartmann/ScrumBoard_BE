from clients.serializers import ClientSerializer
from rest_framework import viewsets
from clients.models import Client
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

# ViewSets define the view behavior.

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    
    
    
    
    
    
    
    
    
    
    # @csrf_exempt
    # def client_list(request):
    #     if request.method == 'GET':
    #         queryset = Client.objects.all()
    #         serializer = ClientSerializer(queryset, many=True)
    #         return JsonResponse(serializer.data, safe=False)
        
    #     elif request.method == 'POST':
    #         data = JSONParser().parse(request)
    #         serializer = ClientSerializer(data=data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return JsonResponse(serializer.data, status=201)
    #         return JsonResponse(serializer.errors, status=400)
    
    # def client_detail(request, pk):
    #     try:
    #         queryset = Client.objects.get(pk=pk)
    #     except Client.DoesNotExist:
    #         return HttpResponse(status=404)

    #     if request.method == 'GET':
    #         serializer = ClientSerializer(queryset)
    #         return JsonResponse(serializer.data)

    #     elif request.method == 'PUT':
    #         data = JSONParser().parse(request)
    #         serializer = ClientSerializer(queryset, data=data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return JsonResponse(serializer.data)
    #         return JsonResponse(serializer.errors, status=400)

    #     elif request.method == 'DELETE':
    #         queryset.delete()
    #         return HttpResponse(status=204)
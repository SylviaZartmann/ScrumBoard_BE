from django.shortcuts import render
from rest_framework import viewsets
from contacts.models import Contact
from contacts.serializers import ContactSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    @csrf_exempt
    def contact_list(request):
        if request.method == 'GET':
            queryset = Contact.objects.all()
            serializer = ContactSerializer(queryset, many=True)
            return JsonResponse(serializer.data, safe=False)
        
        elif request.method == 'POST':
            data = JSONParser().parse(request)
            serializer = ContactSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)
    
    def contact_detail(request, pk):
        try:
            queryset = Contact.objects.get(pk=pk)
        except Contact.DoesNotExist:
            return HttpResponse(status=404)

        if request.method == 'GET':
            serializer = ContactSerializer(queryset)
            return JsonResponse(serializer.data)

        elif request.method == 'PUT':
            data = JSONParser().parse(request)
            serializer = ContactSerializer(queryset, data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
            return JsonResponse(serializer.errors, status=400)

        elif request.method == 'DELETE':
            queryset.delete()
            return HttpResponse(status=204)
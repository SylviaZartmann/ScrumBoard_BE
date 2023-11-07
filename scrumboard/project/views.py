from django.shortcuts import render
from rest_framework import viewsets
from project.models import Project
from project.serializers import ProjectSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

# ViewSets define the view behavior.

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    
    
    
    
    
    
    
    
    # @csrf_exempt
    # def project_list(request):
    #     if request.method == 'GET':
    #         queryset = Project.objects.all()
    #         serializer = ProjectSerializer(queryset, many=True)
    #         return JsonResponse(serializer.data, safe=False)
        
    #     elif request.method == 'POST':
    #         data = JSONParser().parse(request)
    #         serializer = ProjectSerializer(data=data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return JsonResponse(serializer.data, status=201)
    #         return JsonResponse(serializer.errors, status=400)
    
    # def project_detail(request, pk):
    #     try:
    #         queryset = Project.objects.get(pk=pk)
    #     except Project.DoesNotExist:
    #         return HttpResponse(status=404)

    #     if request.method == 'GET':
    #         serializer = ProjectSerializer(queryset)
    #         return JsonResponse(serializer.data)

    #     elif request.method == 'PUT':
    #         data = JSONParser().parse(request)
    #         serializer = ProjectSerializer(queryset, data=data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return JsonResponse(serializer.data)
    #         return JsonResponse(serializer.errors, status=400)

    #     elif request.method == 'DELETE':
    #         queryset.delete()
    #         return HttpResponse(status=204)
# Create your views here.

# class ProjectViewSet(viewsets.ModelViewSet):

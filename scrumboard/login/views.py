from login.serializers import UserSerializer
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser

# ViewSets define the view behavior.
      
@permission_classes([IsAuthenticated, IsAdminUser])
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    @csrf_exempt
    def user_list(self, request):
        if request.method == 'GET':
            queryset = User.objects.all().order_by('lastname')
            serializer = UserSerializer(queryset, many=True)
            return JsonResponse(serializer.data, safe=False)
        
        elif request.method == 'POST':
            if request.user and request.user.is_staff:
                data = JSONParser().parse(request)
                serializer = UserSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse(serializer.data, status=201)
                return JsonResponse(serializer.errors, status=400)
            else:
                return HttpResponse(status=403) 
    
    @csrf_exempt
    def user_detail(self, request, pk):
        try:
            queryset = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return HttpResponse(status=404)

        if request.method == 'GET':
            serializer = UserSerializer(queryset)
            return JsonResponse(serializer.data)

        elif request.method == 'PUT':
            if request.user and request.user.is_staff:
                data = JSONParser().parse(request)
                serializer = UserSerializer(queryset, data=data)
                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse(serializer.data)
                return JsonResponse(serializer.errors, status=400)
            else:
                return HttpResponse(status=403) 

        elif request.method == 'DELETE':
            if request.user and request.user.is_staff:
                queryset.delete()
                return HttpResponse(status=204)
            else:
                return HttpResponse(status=403) 
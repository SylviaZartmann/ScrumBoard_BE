from login.serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken, APIView


from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from rest_framework import permissions, authentication
# from django.views.decorators.csrf import csrf_exempt
# from django.http import JsonResponse, HttpResponse
# from rest_framework.parsers import JSONParser

# ViewSets define the view behavior.
      
#@permission_classes([IsAuthenticated, IsAdminUser])

#class UserView(APIView): #viewsets.ModelViewSet
    #queryset = User.objects.all()
    

    
    
    # for user in User.objects.all():
    #     Token.objects.get_or_create(user=user)
    
class LoginView(APIView):
    serializer_class = UserSerializer
    
    def get(self, request, format=None):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
    
class UserList():
    
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]
    
    def get(self, request, format=None):
        
        """
        Return a list of all users.
        """
        
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)
    
    
    
    
    # @csrf_exempt
    # def user_list(self, request):
    #     if request.method == 'GET':
    #         queryset = User.objects.all().order_by('lastname')
    #         serializer = UserSerializer(queryset, many=True)
    #         return JsonResponse(serializer.data, safe=False)
        
    #     elif request.method == 'POST':
    #         if request.user and request.user.is_staff:
    #             data = JSONParser().parse(request)
    #             serializer = UserSerializer(data=data)
    #             if serializer.is_valid():
    #                 serializer.save()
    #                 return JsonResponse(serializer.data, status=201)
    #             return JsonResponse(serializer.errors, status=400)
    #         else:
    #             return HttpResponse(status=403) 
    
    # @csrf_exempt
    # def user_detail(self, request, pk):
    #     try:
    #         queryset = User.objects.get(pk=pk)
    #     except User.DoesNotExist:
    #         return HttpResponse(status=404)

    #     if request.method == 'GET':
    #         serializer = UserSerializer(queryset)
    #         return JsonResponse(serializer.data)

    #     elif request.method == 'PUT':
    #         if request.user and request.user.is_staff:
    #             data = JSONParser().parse(request)
    #             serializer = UserSerializer(queryset, data=data)
    #             if serializer.is_valid():
    #                 serializer.save()
    #                 return JsonResponse(serializer.data)
    #             return JsonResponse(serializer.errors, status=400)
    #         else:
    #             return HttpResponse(status=403) 

    #     elif request.method == 'DELETE':
    #         if request.user and request.user.is_staff:
    #             queryset.delete()
    #             return HttpResponse(status=204)
    #         else:
    #             return HttpResponse(status=403) 
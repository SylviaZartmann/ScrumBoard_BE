from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from clients.views import ClientViewSet
from login.views import GroupViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('client/', admin.site.urls),
    path('contract/', admin.site.urls),
    path('employee/', admin.site.urls),
    path('project/', admin.site.urls),
    path('contacts/', admin.site.urls),
    path('api/', include('rest_framework.urls')),
    path('', include(router.urls)),
]

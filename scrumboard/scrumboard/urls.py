from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from clients.views import ClientViewSet
from login.views import GroupViewSet, UserViewSet
from contacts.views import ContactViewSet
from contracts.views import ContractViewSet
from employees.views import EmployeeViewSet
from project.views import ProjectViewSet

router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'contracts', ContractViewSet)
router.register(r'contacts', ContactViewSet)
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

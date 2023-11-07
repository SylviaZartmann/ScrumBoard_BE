from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from login.views import LoginView
#from clients.views import ClientViewSet
#from login.views import UserView
#from contacts.views import ContactViewSet
#from contracts.views import ContractViewSet
#from employees.views import EmployeeViewSet
#from project.views import ProjectViewSet

router = routers.DefaultRouter()
#router.register(r'projects', ProjectViewSet, basename='project')
#router.register(r'employees', EmployeeViewSet, basename='employee')
#router.register(r'contracts', ContractViewSet, basename='contract')
#router.register(r'contacts', ContactViewSet, basename='contact')
#router.register(r'clients', ClientViewSet, basename='client')
#router.register(r'users', UserView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('rest_framework.urls')),
    path('', include(router.urls)),
    path('login/', LoginView.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

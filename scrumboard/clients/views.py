from clients.serializers import ClientSerializer
from rest_framework import viewsets
from project.models import Project

# ViewSets define the view behavior.
class ClientViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ClientSerializer
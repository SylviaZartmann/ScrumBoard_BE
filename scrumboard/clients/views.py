from clients.serializers import ClientSerializer
from rest_framework import viewsets
from clients.models import Client

# ViewSets define the view behavior.
class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
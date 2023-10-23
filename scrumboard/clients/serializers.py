from rest_framework import serializers
from clients.models import Client

    
    # Serializers define the API representation.
class ClientSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Client
        fields = ['url', 'name', 'phone', 'first_contact', 'origin_city', 'origin_street', 'origin_post_code', 'contact_person']
        
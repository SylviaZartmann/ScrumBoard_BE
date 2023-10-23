from rest_framework import serializers
from contacts.models import Contact

    
    # Serializers define the API representation.
class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = ['url', 'firstname', 'lastname', 'email', 'phone', 'company', 'color']
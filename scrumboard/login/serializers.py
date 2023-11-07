from django.contrib.auth.models import User
from rest_framework import serializers

# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
#token anlegen zur registrierung bzw. validierung der person, die was machen darf
# auth token
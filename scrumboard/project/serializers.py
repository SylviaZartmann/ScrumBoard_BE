from project.models import Project
from rest_framework import serializers


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ['url', 'firstname', 'lastname', 'email', 'phone', 'origin_city', 'origin_street', 'origin_post_code', 'profession', 'entry_date', 'leaving_date', 'working_hours', 'salary', 'color', 'current_project']
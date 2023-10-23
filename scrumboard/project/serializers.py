from project.models import Project
from rest_framework import serializers


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ['url', 'name', 'shortage', 'project_lead', 'project_team', 'client', 'processing_time', 'date_start', 'date_end', 'features']
from django.db import models
from clients.models import Client

# Create your models here.
class Project(models.Model):
    name = models.CharField(default='', max_length=50)
    shortage = models.CharField(default='', max_length=5)
    project_lead = models.ForeignKey('employees.Employee', on_delete=models.SET_NULL, null=True, default='', related_name='lead_projects')
    project_team = models.ManyToManyField('employees.Employee', default='', related_name='team_projects')
    client = models.OneToOneField(Client, on_delete=models.SET_NULL, default='', null=True)
    processing_time = models.DurationField(default='')
    date_start = models.DateField(default=None, blank=False, null=True)
    date_end = models.DateField(default=None, blank=False, null=True)
    features = models.CharField(default='', max_length=500)
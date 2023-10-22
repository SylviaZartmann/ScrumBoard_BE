from django.db import models
from clients.models import Client
from employees.models import Employee

# Create your models here.
class Project(models.Model):
    name = models.CharField(default='', max_length=50)
    shortage = models.CharField(default='', max_length=5)
    project_lead = models.ForeignKey(Employee, on_delete=models.SET_NULL, default='')
    project_team = models.ManyToManyField(Employee, default='')
    contractor = models.ForeignKey(Employee, on_delete=models.SET_NULL, related_name='contractor', limit_choices_to={'designation': 'Geschäftsführung'}, default='')
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, default='')
    processing_time = models.DurationField(default='')
    date_start = models.DateField(default=None, blank=False, null=True)
    date_end = models.DateField(default=None, blank=False, null=True)
    features = models.CharField(default='', max_length=500)
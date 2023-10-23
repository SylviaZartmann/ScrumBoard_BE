from django.db import models
from clients.models import Client
from employees.models import Employee


# Create your models here.
class Contract(models.Model):
    CONTRACTING_KINDS = [
        ('estimation', 'Kostenschätzung'),
        ('calculation', 'Kostenberechnung'),
        ('tender', 'Ausschreibung'),
    ]
        
    number = models.CharField(default='', max_length=10)
    contracting_date = models.DateField(default=None, blank=False, null=True)
    contracting_kind = models.CharField(max_length=20, choices=CONTRACTING_KINDS, default="")
    order_value = models.IntegerField(default='')
    contractor = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name='contractor', limit_choices_to={'designation': 'Geschäftsführung'}, default='')
    client = models.ForeignKey(Client, default='', on_delete=models.SET_NULL, null=True)
    date_start = models.DateField(default=None, blank=False, null=True)
    date_end = models.DateField(default=None, blank=False, null=True)
    precessing_time = models.DurationField(default='')
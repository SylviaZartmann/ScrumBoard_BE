from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Employee(models.Model):
    PROFESSION_CHOICE = [
        ('lead', 'Geschäftsführung'),
        ('architect', 'Architekt'),
        ('ingenieur', 'Bauingenieur'),
        ('technician', 'Bautechniker'),
        ('backoffice', 'backoffice'),
        ('freelancer', 'Freiberufliche'),
        ('other', 'Andere'),
    ]
    
    
    firstname = models.CharField(default='', max_length=50)
    lastname = models.CharField(default='', max_length=50)
    email = models.EmailField(default='')
    phone = PhoneNumberField(default='')
    origin_city = models.CharField(max_length=50)
    origin_street = models.CharField(max_length=50)
    origin_post_code = models.CharField(max_length=50)
    profession = models.CharField(default='', choices=PROFESSION_CHOICE, max_length=50)
    entry_date = models.DateField(default=None, blank=False, null=True)
    leaving_date = models.DateField(default=None, blank=False, null=True)
    working_hours = models.IntegerField(default='')
    salary = models.IntegerField(default='')
    color = models.CharField(default="#000000", max_length=7)
    current_project = models.ManyToManyField('project.Project', default='')
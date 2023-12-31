from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Contact(models.Model):
    firstname = models.CharField(default='', max_length=50)
    lastname = models.CharField(default='', max_length=50)
    email = models.EmailField(default='')
    phone = PhoneNumberField(default='')
    company= models.OneToOneField('clients.Client', default='', on_delete=models.SET_NULL, null=True, blank=True)
    color = models.CharField(default="#000000", max_length=7)
    
    def __str__(self):
        return self.firstname + ' ' + self.lastname
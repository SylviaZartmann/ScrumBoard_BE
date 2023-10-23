from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=150)
    phone = PhoneNumberField(default='')
    first_contact = models.DateField(default='')
    origin_city = models.CharField(max_length=50)
    origin_street = models.CharField(max_length=50)
    origin_post_code = models.CharField(max_length=50)
    contact_person = models.OneToOneField('contacts.Contact', default='', on_delete=models.SET_NULL, null=True, blank=True)
    class Meta:
        ordering = ['name']
    
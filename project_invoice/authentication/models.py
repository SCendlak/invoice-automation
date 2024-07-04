from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=255, help_text='Company name', blank=True, null=True)
    nip = models.CharField(max_length=50, help_text='Nip number', blank=True, null=True)
    name = models.CharField(max_length=255, help_text='Company name max 255', blank=True, null=True)
    street_address = models.CharField(max_length=255, help_text='Street name and building number max 255', blank=True,
                                      null=True)
    postal_code = models.CharField(max_length=20, help_text='Postal code', blank=True, null=True)
    city = models.CharField(max_length=100, help_text='City', blank=True, null=True)
    voivodeship = models.CharField(max_length=100, help_text='Voivodeship', blank=True, null=True)
    country = models.CharField(max_length=100, help_text='Country', blank=True, null=True)
    bank_name = models.CharField(max_length=255, help_text='Bank name', blank=True, null=True)
    bank_address = models.CharField(max_length=255, help_text='Bank address', blank=True, null=True)
    iban = models.CharField(max_length=34, help_text='IBAN', blank=True, null=True)
    swift = models.CharField(max_length=11, help_text='SWIFT', blank=True, null=True)

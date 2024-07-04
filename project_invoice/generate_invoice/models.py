from django.db import models
from django.urls import reverse

# Create your models here.


class Contact(models.Model):

    name = models.CharField(max_length=255, help_text='Company name max 255')
    street = models.CharField(max_length=255, help_text='Street name and building number max 255', blank=True, null=True)
    postal_code = models.CharField(max_length=20, help_text='Postal code', blank=True, null=True)
    city = models.CharField(max_length=100, help_text='City', blank=True, null=True)
    voivodeship = models.CharField(max_length=100, help_text='Voivodeship', blank=True, null=True)
    country = models.CharField(max_length=100, help_text='Country', blank=True, null=True)
    iban = models.CharField(max_length=34, help_text='IBAN', blank=True, null=True)
    swift = models.CharField(max_length=11, help_text='SWIFT', blank=True, null=True)
   
    class META:
        ordering = ['-name']

    def get_absolute_url(self):
        """Returns the URL to access a particular instance of MyModelName."""
        return reverse('invoice:contact-details', args=[str(self.name)], current_app='invoice')

    def __str__(self):
        return self.name


class Products(models.Model):
    index = models.IntegerField(blank=True, null=True)
    cena = models.CharField(max_length=255,blank=True, null=True)
    nazwa = models.CharField(max_length=255,blank=True, null=True)
    waga = models.CharField(max_length=255,blank=True, null=True)
    kodcelny = models.IntegerField(blank=True, null=True)


class Invoice(models.Model):
    title = models.CharField(max_length=255)
    index = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)

# forms.py
from django import forms
from .models import Contact


class UploadBaseInvoiceForm(forms.Form):
    file = forms.FileField(label='PDF', required=True, widget=forms.FileInput(attrs={'accept': 'application/pdf'}))


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'street', 'postal_code', 'city', 'voivodeship', 'country', 'iban', 'swift']


class InvoiceForm(forms.Form):
    contacts = Contact.objects.all()
    incoterms_list = [
        ('EXW', 'EXW EX Works'),
        ('FCA', 'FCA Free Carrier'),
        ('CPT', 'CPT Carriage Paid To'),
        ('CIP', 'CIP Carriage and Insurance Paid To '),
        ('DAP', 'DAP Delivered at Place'),
        ('DPU', 'DPU Delivered at Place Unloaded'),
        ('DDP', 'DDP Delivered Duty Paid')
    ]
    buyer = forms.ChoiceField(label='Kupiec', choices=[(contact.id, contact.name) for contact in contacts],
                              widget=forms.Select())
    sellingDate = forms.DateField(label='Data sprzedazy', widget=forms.DateInput(attrs={'type': 'date'}))
    sellingPlace = forms.CharField(label='Miejsce sprzedazy', max_length=16, required=False)
    car_plate = forms.CharField(label='Numery auta', max_length=16, required=False)
    incoterms = forms.ChoiceField(choices=incoterms_list, widget=forms.Select())
    incoterms_place = forms.CharField(label='Miejsce Incoterms', max_length=255, required=False)
    payment_time = forms.CharField(label='Termin Płatności', max_length=255, required=False)
    notes = forms.CharField(label='Uwagi', max_length=255, required=False)

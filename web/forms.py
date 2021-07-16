from django import forms
from django.db.models.base import Model
from django.forms import fields
from django.forms import widgets
from django.utils.translation import ugettext_lazy as _
from .models import Contact
from django.forms.widgets import DateInput, SelectMultiple, TextInput, Textarea, EmailInput, CheckboxInput, URLInput, Select, NumberInput, RadioSelect, FileInput


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Name'}),
            'subject': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Subject'}),
            'location': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Location'}),
            'email': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Email'}),
            'number': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Phone Number'}),
            'whatsapp_number': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Whatsapp Number'}),
            'date': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Date'}),
            'time': Select(attrs={'class': 'required form-control select', 'placeholder': 'Time'}),
        }

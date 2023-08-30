from django import forms
from django.forms import ModelForm, DateField, widgets

from main.models import *


class AddSampleForm(ModelForm):
    class Meta:
        model = Sample
        fields = (
            'tracking_id',
            'sample_owner',
            'centre_owner',
            'group_owner',
            'client_site',
            'sample_location',
            'hazard_advice',
            'date_received',
            'sample_status',
            'description',

        )
        labels = {
            'tracking_id': 'Sample Tracking ID',
            'sample_owner': 'Sample Owner',
            'centre_owner': 'Research Centre',
            'group_owner': 'Group',
            'client_site': 'Client Site',
            'sample_location': 'Storage Location',
            'hazard_advice': 'Hazard Advice Provided',
            'date_received': 'Date Received',
            'sample_status': 'Status of Sample',
            'description': 'Description',

        }
        widgets = {
            'company_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Required'}),
            'date_received': widgets.DateInput(attrs={'type': 'date', 'class': 'short-field'}),
        }


class AddSampleLocationForm(ModelForm):
    class Meta:
        model = Location
        fields = (
            'location',
            'description',
        )
        widgets = {
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Required'}),
        }


class AddSampleClientForm(ModelForm):
    class Meta:
        model = Client
        fields = (
            'company_name',
            'site_name',
            'site_contact_name',
            'site_contact_email',
            'description',

        )
        labels = {
            'company_name': 'Company Name',
            'site_name': 'Site Name',
            'site_contact_name': 'Site Contact Name',
            'site_contact_email': 'Site Contact Email',
            'description': 'Description',
        }
        widgets = {
            'company_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Required'}),
        }


from django import forms
from django.forms import ModelForm, DateField, widgets

from main.models import *


class AddSampleForm(ModelForm):
    client = forms.ModelChoiceField(queryset=Client.objects.all())
    sample_location = forms.ModelMultipleChoiceField(queryset=Location.objects.all(), widget=forms.CheckboxSelectMultiple,)

    class Meta:
        model = Sample
        fields = (
            'tracking_id',
            'sample_owner',
            'centre_owner',
            'group_owner',
            'client',
            'client_site',
            'client_contact',
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


        )
        labels = {
            'company_name': 'Company Name',

        }
        widgets = {
            'company_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Required'}),
        }


class AddSampleClientSiteForm(ModelForm):
    company_name = forms.ModelChoiceField(queryset=Client.objects.all())
    class Meta:
        model = ClientSite
        fields = (
            'company_name',
            'site_name',


        )
        labels = {
            'company_name': 'Company Name',
            'site_name': 'Site Name',

        }
        widgets = {
            'company_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Required'}),
        }


class AddSampleClientContactForm(ModelForm):
    company_name = forms.ModelChoiceField(queryset=Client.objects.all())
    site_name = forms.ModelChoiceField(queryset=ClientSite.objects.all())
    class Meta:
        model = ClientContact
        fields = (
            'company_name',
            'site_name',
            'client_name',
            'client_number',
            'client_email',


        )
        labels = {
            'company_name': 'Company Name',
            'site_name': 'Site Name',
            'client_name': 'Client Name',
            'client_number': 'Client Number',
            'client_email': 'Client Email',

        }
        widgets = {
            'company_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Required'}),
        }

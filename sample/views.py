from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import timedelta, datetime
from django.db.models.functions import ExtractYear, ExtractMonth
from calendar import month_name
from django.db.models import Count

from main.models import *
from .forms import *

# Create your views here.


@login_required(login_url='main_app:login')
def sample_home(request):
    samples = Sample.objects.all()
    context = {
        'samples': samples,

    }
    return render(request, 'sample/sample_home.html', context)


@login_required(login_url='main_app:login')
def add_sample(request):
    samples = Sample.objects.all()
    if request.method == "POST":
        form = AddSampleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sample_app:sample_home')
    else:
        form = AddSampleForm()
    context = {
        'form': form,
    }
    return render(request, 'sample/add_sample.html',context)


@login_required(login_url='main_app:login')
def delete_sample(request, sample_id):
    samples = Sample.objects.get(pk=sample_id)
    samples.delete()
    return redirect('sample_app:sample_home')


@login_required(login_url='main_app:login')
def sample_location(request):

    locations = Location.objects.all().order_by('location')

    if request.method == 'POST':
        form = AddSampleLocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sample_app:sample_location')
    else:
        form = AddSampleLocationForm


    context = {
        'locations': locations,
        'form': form,

    }
    return render(request, 'sample/sample_location.html', context)


@login_required(login_url='main_app:login')
def edit_sample_location(request, location_id):
    locations = Location.objects.get(pk=location_id)
    form = AddSampleLocationForm(request.POST or None, instance=locations)
    if form.is_valid():
        form.save()
        return redirect('sample_app:sample_location')

    context = {
        'form': form,
    }
    return render(request, 'sample/edit_sample_location.html',context)


@login_required(login_url='main_app:login')
def delete_sample_location(request, location_id):
    locations = Location.objects.get(pk=location_id)
    locations.delete()
    return redirect('sample_app:sample_location')


@login_required(login_url='main_app:login')
def sample_client(request):

    clients = Client.objects.all().order_by('company_name')

    if request.method == 'POST':
        form = AddSampleClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sample_app:sample_client')
    else:
        form = AddSampleClientForm


    context = {
        'clients': clients,
        'form': form,

    }
    return render(request, 'sample/sample_client.html', context)


@login_required(login_url='main_app:login')
def edit_sample_client(request, client_id):
    clients = Client.objects.get(pk=client_id)
    form = AddSampleClientForm(request.POST or None, instance=clients)
    if form.is_valid():
        form.save()
        return redirect('sample_app:sample_client')

    context = {
        'form': form,
    }
    return render(request, 'sample/edit_sample_client.html',context)


@login_required(login_url='main_app:login')
def delete_sample_client(request, client_id):
    clients = Client.objects.get(pk=client_id)
    clients.delete()
    return redirect('sample_app:sample_client')


@login_required(login_url='main_app:login')
def sample_client_site(request):

    client_sites = ClientSite.objects.all().order_by('site_name')

    if request.method == 'POST':
        form = AddSampleClientSiteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sample_app:sample_client_site')
    else:
        form = AddSampleClientSiteForm


    context = {
        'client_sites': client_sites,
        'form': form,

    }
    return render(request, 'sample/sample_client_site.html', context)


@login_required(login_url='main_app:login')
def sample_client_contact(request):

    client_contacts = ClientContact.objects.all().order_by('company_name')

    if request.method == 'POST':
        form = AddSampleClientContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sample_app:sample_client_contact')
    else:
        form = AddSampleClientContactForm


    context = {
        'client_contacts': client_contacts,
        'form': form,

    }
    return render(request, 'sample/sample_client_contact.html', context)

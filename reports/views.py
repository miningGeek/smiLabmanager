from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import timedelta, datetime
from django.db.models.functions import ExtractYear, ExtractMonth
from calendar import month_name
from django.db.models import Count

from main.models import Booking, Project, PrestartCheck
# Create your views here.

def report_home(request):
    today = timezone.now().date()
    twelve_months_ago = today - timedelta(days=365)

    # Retrieve booking data for the last 12 months
    bookings = Booking.objects.filter(start_date__gte=twelve_months_ago)

    # Calculate total hours for each month
    months_hours = {}
    for booking in bookings:
        month = booking.start_date.strftime('%Y-%m')
        hours = booking.num_hours
        if month in months_hours:
            months_hours[month] += hours
        else:
            months_hours[month] = hours

     # Calculate number of projects for each month
    months_projects = Booking.objects.filter(start_date__gte=twelve_months_ago) \
        .exclude(proj_data=None) \
        .annotate(month=ExtractMonth('start_date'), year=ExtractYear('start_date')) \
        .values('year', 'month') \
        .annotate(projects_count=Count('proj_data', distinct=True))

    # Calculate number of prestarts for each month
    months_prestart = PrestartCheck.objects.filter(prestart_date__gte=twelve_months_ago) \
        .values('prestart_date__year', 'prestart_date__month') \
        .annotate(month=ExtractMonth('prestart_date'), year=ExtractYear('prestart_date')) \
        .annotate(count=Count('id')) \
        .order_by('prestart_date__year', 'prestart_date__month')

    # Prepare data for chart

    labels_hours = [datetime.strptime(month, '%Y-%m').strftime('%m-%Y') for month in months_hours.keys()]
    data_hours = list(months_hours.values())

    labels_projects = [datetime(month['year'], month['month'], 1).strftime('%m-%Y') for month in months_projects]
    data_projects = [month['projects_count'] for month in months_projects]

    labels_prestart = [f"{month['month']}-{month['year']}" for month in months_prestart]
    data_prestart = [month['count'] for month in months_prestart]

    labels_hours.reverse()
    data_hours.reverse()

    context = {
        'labels_hours': labels_hours,
        'data_hours': data_hours,
        'labels_projects': labels_projects,
        'data_projects': data_projects,
        'labels_prestart': labels_prestart,
        'data_prestart': data_prestart,
    }


    return render(request, 'reports/report_home.html', context)
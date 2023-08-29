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


@login_required(login_url='main_app:login')
def report_home(request):
    today = timezone.now().date()
    twelve_months_ago = today - timedelta(days=365)
    three_months_ago = today - timedelta(days=90)

    # Retrieve booking data for the last 12 months
    bookings = Booking.objects.filter(start_date__gte=twelve_months_ago)
    bookings_days = Booking.objects.filter(start_date__gte = three_months_ago)

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

    # Calculate number of bookings per day for last 3 months
    booking_count_per_day = {}
    for booking in bookings_days:
        day = booking.start_date
        if day in booking_count_per_day:
            booking_count_per_day[day]+=1
        else:
            booking_count_per_day[day] =1

    # Prepare data for chart

    labels_hours = [datetime.strptime(month, '%Y-%m').strftime('%m-%Y') for month in months_hours.keys()]
    data_hours = list(months_hours.values())
    sorted_hours_data = sorted(zip(labels_hours, data_hours), key=lambda x: x[0])

    # Unpack the sorted data
    labels_hours = [label for label, _ in sorted_hours_data]
    data_hours = [data for _, data in sorted_hours_data]

    labels_projects = sorted([datetime(month['year'], month['month'], 1).strftime('%m-%Y') for month in months_projects])
    data_projects = [month['projects_count'] for month in months_projects]

    labels_prestart = sorted([f"{month['month']}-{month['year']}" for month in months_prestart])
    data_prestart = [month['count'] for month in months_prestart]

    #labels_days = list(booking_count_per_day.keys())
    labels_days = [day.strftime('%d-%m-%y') for day in booking_count_per_day.keys()]
    data_days = list(booking_count_per_day.values())

    #labels_hours.reverse()
    #data_hours.reverse()

    context = {
        'labels_hours': labels_hours,
        'data_hours': data_hours,
        'labels_projects': labels_projects,
        'data_projects': data_projects,
        'labels_prestart': labels_prestart,
        'data_prestart': data_prestart,
        'labels_days': labels_days,
        'data_days': data_days,
    }


    return render(request, 'reports/report_home.html', context)


@login_required(login_url='main_app:login')
def report_jkmrc(request):
    today = timezone.now().date()

    twelve_months_ago = today - timedelta(days=365)
    three_months_ago = today - timedelta(days=90)

    # Retrieve booking data for the last 12 months
    bookings = Booking.objects.filter(start_date__gte=twelve_months_ago, group__centres__name='JKMRC')
    bookings_days = Booking.objects.filter(start_date__gte=three_months_ago)

    # Calculate total hours for each month
    months_hours = {}
    for booking in bookings:
        month = booking.start_date.strftime('%Y-%m')
        hours = booking.num_hours
        if month in months_hours:
            months_hours[month] += hours
        else:
            months_hours[month] = hours

    labels_hours = [datetime.strptime(month, '%Y-%m').strftime('%m-%Y') for month in months_hours.keys()]
    data_hours = list(months_hours.values())
    sorted_hours_data = sorted(zip(labels_hours, data_hours), key=lambda x: x[0])

    # Unpack the sorted data
    labels_hours = [label for label, _ in sorted_hours_data]
    data_hours = [data for _, data in sorted_hours_data]

    context = {
        'labels_hours': labels_hours,
        'data_hours': data_hours,
    }
    return render(request, 'reports/report_jkmrc.html', context)


@login_required(login_url='main_app:login')
def report_jktech(request):
    today = timezone.now().date()

    twelve_months_ago = today - timedelta(days=365)
    three_months_ago = today - timedelta(days=90)

    # Retrieve booking data for the last 12 months
    bookings = Booking.objects.filter(start_date__gte=twelve_months_ago, group__centres__name='JKTech')
    bookings_days = Booking.objects.filter(start_date__gte=three_months_ago)

    # Calculate total hours for each month
    months_hours = {}
    for booking in bookings:
        month = booking.start_date.strftime('%Y-%m')
        hours = booking.num_hours
        if month in months_hours:
            months_hours[month] += hours
        else:
            months_hours[month] = hours

    labels_hours = [datetime.strptime(month, '%Y-%m').strftime('%m-%Y') for month in months_hours.keys()]
    data_hours = list(months_hours.values())
    sorted_hours_data = sorted(zip(labels_hours, data_hours), key=lambda x: x[0])

    # Unpack the sorted data
    labels_hours = [label for label, _ in sorted_hours_data]
    data_hours = [data for _, data in sorted_hours_data]

    context = {
        'labels_hours': labels_hours,
        'data_hours': data_hours,
    }
    return render(request, 'reports/report_jktech.html', context)
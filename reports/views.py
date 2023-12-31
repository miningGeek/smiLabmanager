from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login, logout
from django.http import HttpResponseRedirect, HttpResponse, response
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import timedelta, datetime, date
from django.db.models.functions import ExtractYear, ExtractMonth, TruncDate
from calendar import month_name
from django.db.models import Count
from collections import defaultdict
import csv

from main.models import Booking, Project, PrestartCheck, Equipment
# Create your views here.


@login_required(login_url='main_app:login')
def report_home(request):
    today = timezone.now().date()
    twelve_months_ago = today - timedelta(days=365)
    three_months_ago = today - timedelta(days=90)

    # Retrieve booking data for the last 12 months
    #bookings = Booking.objects.filter(start_date__gte=twelve_months_ago)
    bookings =Booking.objects.filter(start_date__gte=three_months_ago).exclude(
        status__in=['Cancelled', 'Rejected'])
    #bookings_days = Booking.objects.filter(start_date__gte = three_months_ago)
    bookings_days = Booking.objects.filter(start_date__gte=three_months_ago).exclude(
        status__in=['Cancelled', 'Rejected'])

    #ps_days = PrestartCheck.objects.filter(prestart_date__gte = three_months_ago)
    # Calculate number of prestarts per day for last 3 months
    ps_days = PrestartCheck.objects \
        .filter(prestart_date__gte=three_months_ago) \
        .annotate(day=TruncDate('prestart_date')) \
        .values('day') \
        .annotate(count=Count('id')) \
        .order_by('day')


    # Calculate total hours for each month
    months_hours = {}
    for booking in bookings:
        month = booking.start_date.strftime('%Y-%m')
        hours = booking.num_hours
        if hours is None:
            hours = 0
        if month in months_hours:
            months_hours[month] += hours
        else:
            months_hours[month] = hours

    pp_bookings = Booking.objects.filter(
        start_date__gte=twelve_months_ago,
        equip_name__group_owner__name = 'Pilot Plant'
    )
    pp_months_hours = {}
    for booking in pp_bookings:
        pp_month = booking.start_date.strftime('%Y-%m')
        pp_hours = booking.num_hours
        if pp_hours is None:
            pp_hours = 0
        if pp_month in pp_months_hours:
            pp_months_hours[pp_month] += pp_hours
        else:
            pp_months_hours[pp_month] = pp_hours

    jkt_bookings = Booking.objects.filter(
        start_date__gte=twelve_months_ago,
        equip_name__group_owner__name='JKTech Lab'
    )
    jkt_months_hours = {}
    for booking in jkt_bookings:
        jkt_month = booking.start_date.strftime('%Y-%m')
        jkt_hours = booking.num_hours
        if jkt_hours is None:
            jkt_hours = 0
        if jkt_month in jkt_months_hours:
            jkt_months_hours[jkt_month] += jkt_hours
        else:
            jkt_months_hours[jkt_month] = jkt_hours

    comb_bookings = Booking.objects.filter(
        start_date__gte=twelve_months_ago,
        equip_name__group_owner__name='JKMRC/JKTech'
    )
    comb_months_hours = {}
    for booking in comb_bookings:
        comb_month = booking.start_date.strftime('%Y-%m')
        comb_hours = booking.num_hours
        if comb_hours is None:
            comb_hours = 0
        if comb_month in comb_months_hours:
            comb_months_hours[comb_month] += comb_hours
        else:
            comb_months_hours[comb_month] = comb_hours

    sep_bookings = Booking.objects.filter(
        start_date__gte=twelve_months_ago,
        equip_name__group_owner__name='Separation'
    )
    sep_months_hours = {}
    for booking in sep_bookings:
        sep_month = booking.start_date.strftime('%Y-%m')
        sep_hours = booking.num_hours
        if sep_hours is None:
            sep_hours = 0
        if sep_month in sep_months_hours:
            sep_months_hours[sep_month] += sep_hours
        else:
            sep_months_hours[sep_month] = sep_hours

    chem_bookings = Booking.objects.filter(
        start_date__gte=twelve_months_ago,
        equip_name__group_owner__name='Flotation Chemistry'
    )
    chem_months_hours = {}
    for booking in chem_bookings:
        chem_month = booking.start_date.strftime('%Y-%m')
        chem_hours = booking.num_hours
        if chem_hours is None:
            chem_hours = 0
        if chem_month in chem_months_hours:
            chem_months_hours[chem_month] += chem_hours
        else:
            chem_months_hours[chem_month] = chem_hours

    appco_bookings = Booking.objects.filter(
        start_date__gte=twelve_months_ago,
        equip_name__group_owner__name='Advanced Process Prediction and Control'
    )
    appco_months_hours = {}
    for booking in appco_bookings:
        appco_month = booking.start_date.strftime('%Y-%m')
        appco_hours = booking.num_hours
        if appco_hours is None:
            appco_hours = 0
        if appco_month in appco_months_hours:
            appco_months_hours[appco_month] += appco_hours
        else:
            appco_months_hours[appco_month] = appco_hours

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

    # Calculate number of prestarts per day for last 3 months
    # ps_count_per_day = {}
    # for prestart in ps_days:
    #     day = prestart.prestart_date
    #     if day in ps_count_per_day:
    #         ps_count_per_day[day] +=1
    #     else:
    #         ps_count_per_day[day]=1

    # Calculate number of prestarts per day for last 3 months
    # Create a dictionary to store the counts per day
    ps_count_per_day = defaultdict(int)

    # Calculate number of prestarts for each day within the last 3 months
    # for prestart in ps_days:
    #      day = prestart.prestart_date.date()  # Get the date part without time
    #      ps_count_per_day[day] += 1

    for prestart_day in ps_days:
        day = prestart_day['day'].strftime('%Y-%m-%d')  # Format the date as a string
        ps_count_per_day[day] += 1

    # Convert the defaultdict to a regular dictionary
    ps_count_per_day = dict(ps_count_per_day)

    # Sort the dictionary by date if needed
    sorted_ps_count_per_day = dict(sorted(ps_count_per_day.items()))


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

    # labels for prestart days over last 3 months
    #labels_ps_days = [day.strftime('%d-%m-%y') for day in ps_count_per_day.keys()]
    #labels_ps_days = [day['day'].strftime('%d-%m-%y') for day in ps_days]
    #data_ps_days = list(ps_count_per_day.values())
    labels_ps_days = [day['day'].strftime('%d-%m-%y') for day in ps_days]
    data_ps_days = [day['count'] for day in ps_days]


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
        'labels_ps_days': labels_ps_days,
        'data_ps_days': data_ps_days,
        'pp_months_hours': pp_months_hours,
        'jkt_months_hours': jkt_months_hours,
        'comb_months_hours': comb_months_hours,
        'sep_months_hours': sep_months_hours,
        'chem_months_hours': chem_months_hours,
        'appco_months_hours': appco_months_hours,
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
        if hours is None:
            hours = 0
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
        if hours is None:
            hours = 0
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


# Generate csv file bookings
def bookings_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Diposition'] = 'attachment; filename=bookings.csv'

    # Create a csv writer
    writer = csv.writer(response)

    # Designate bookings model
    bookings = Booking.objects.all()

    # Add column headings to csv file
    writer.writerow(['User Name', 'Project Name', 'Request Date', 'Group', 'Equipment Name', 'Start Date', 'Shift', 'Num of Hours', 'Status'])

    # loop through Booking and output to csv
    for booking in bookings:
        writer.writerow([booking.user_name, booking.proj_data, booking.request_date, booking.group, booking.equip_name, booking.start_date, booking.shift, booking.num_hours, booking.status])

    return response


def equipment_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Diposition'] = 'attachment; filename=equipment.csv'

    # Create a csv writer
    writer = csv.writer(response)

    # Designate bookings model
    equipments = Equipment.objects.all()

    # Add column headings to csv file
    writer.writerow(
        ['Equipment Name', 'Description', 'Room', 'Building Level', 'Building', 'Is Equipment', 'Equipment Group', 'Group'])

    # loop through Booking and output to csv
    for equipment in equipments:
        writer.writerow([equipment.equip_name, equipment.description, equipment.room, equipment.building_level, equipment.building, equipment.is_equip, equipment.equip_group, equipment.group_owner])

    return response


def prestart_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Diposition'] = 'attachment; filename=prestart.csv'

    # Create a csv writer
    writer = csv.writer(response)

    # Designate bookings model
    prestarts = PrestartCheck.objects.all()

    # Add column headings to csv file
    writer.writerow(
        ['User Name', 'Equipment', 'Prestart Date', 'Trained', 'SOP RA', 'Test Tag', 'Elect Lead', 'Stop Button',
         'Safety Stop', 'guarding', 'interlock', 'Rubber Strap', 'Dust Extract', 'Counter', 'Hyd Pump', 'Hyd Oil Level', 'Water Electrical', 'Water Level',
         'Air Pressure', 'Cable', 'Seals', 'Drainage', 'Housekeeping', 'Anti Slip Mats', 'Noise Baffles', 'Filter Mat', 'Glass Bottle', 'Fume Filter', 'Battery Water', 'Battery Cond', 'Comments'])

    # loop through Booking and output to csv
    for prestart in prestarts:
        writer.writerow([prestart.username, prestart.equip_name, prestart.prestart_date, prestart.trained, prestart.sop_ra, prestart.test_tag, prestart.elect_lead,
                         prestart.stop_button, prestart.safety_stop, prestart.guarding, prestart.interlock, prestart.rubber_strap,
                         prestart.dust_extract, prestart.counter, prestart.hyd_pump, prestart.hyd_oil_level, prestart.water_elect,
                         prestart.water_level, prestart.air_pressure, prestart.cable, prestart.seals, prestart.drainage, prestart.housekeeping,
                         prestart.anti_slip, prestart.noise_baffles, prestart.filter_mat, prestart.glass_bott, prestart.fume_filter,
                         prestart.battery_water, prestart.battery_condition, prestart.comments])

    return response
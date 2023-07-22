from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Q
from django.forms import formset_factory
import json
from django.http import JsonResponse


from django.utils.safestring import mark_safe
import calendar
from django.views import generic
from django.utils import timezone
from datetime import datetime, timedelta, date

from datetime import datetime

from .models import Building, BuildingLevel, Rooms, Equipment,\
    ResearchCentres, Group, Booking, StatusChoice
from .forms import AddBuildingForm, AddBuildingLevelForm, AddBuildingRoomForm, AddEquipmentForm, AddResearchCentreForm, \
    AddGroupForm, AddBookingForm, StatusChoiceForm

from .utils import Calendar
# Create your views here.


def home(request):
    bookings = Booking.objects.all()

    context = {
        'bookings': bookings,
    }

    return render(request, 'main/home.html', context)


def building_list(request):
    build_lists = Building.objects.all()

    if request.method == "POST":
        form = AddBuildingForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('building_list')
    else:
        form = AddBuildingForm

    context = {
        'build_lists': build_lists,
        'form': form
    }
    return render(request, 'main/building_list.html', context)


def edit_building_list(request, building_id):
    build_lists = Building.objects.get(pk=building_id)
    form = AddBuildingForm(request.POST or None, instance=build_lists)
    if form.is_valid():
        form.save()
        return redirect('main_app:edit_building_list')
    context = {
        'form': form
    }
    return render(request, 'main/edit_building_list.html', context)


def delete_building_list(request, building_id):
    build_lists = Building.objects.get(pk=building_id)
    build_lists.delete()
    return redirect('main_app:building_list')


def build_level(request):
    build_levels = BuildingLevel.objects.all()

    if request.method == "POST":
        form = AddBuildingLevelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main_app:build_level')
    else:
        form = AddBuildingLevelForm

    context = {
        'build_levels': build_levels,
        'form': form
    }
    return render(request, 'main/build_level.html', context)


def edit_build_level(request, level_id):
    build_levels = BuildingLevel.objects.get(pk=level_id)
    form = AddBuildingLevelForm(request.POST or None, instance=build_levels)
    if form.is_valid():
        form.save()
        return redirect('main_app:build_level')
    context = {
        'form': form
    }
    return render(request, 'main/build_level.html', context)


def delete_build_level(request, level_id):
    build_levels = BuildingLevel.objects.get(pk=level_id)
    build_levels.delete()
    return redirect('main_app:build_level')


def build_room(request):
    build_rooms = Rooms.objects.all()

    if request.method == "POST":
        form = AddBuildingRoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main_app:build_room')
    else:
        form = AddBuildingRoomForm

    context = {
        'build_rooms': build_rooms,
        'form': form
    }
    return render(request, 'main/build_room.html', context)


def edit_build_room(request, room_id):
    build_rooms = Rooms.objects.get(pk=room_id)
    form = AddBuildingRoomForm(request.POST or None, instance=build_rooms)
    if form.is_valid():
        form.save()
        return redirect('main_app:build_room')
    context = {
        'form': form
    }
    return render(request, 'main/build_room.html', context)


def delete_build_room(request, room_id):
    build_levels = Rooms.objects.get(pk=room_id)
    build_levels.delete()
    return redirect('main_app:build_room')


def equip_list(request):
    equip_lists = Equipment.objects.all()

    if request.method == "POST":
        form = AddEquipmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main_app:equip_list')
    else:
        form = AddEquipmentForm

    context = {
        'equip_lists': equip_lists,
        'form': form
    }
    return render(request, 'main/equip_list.html', context)


def edit_equip_list(request, equip_id):
    equip_lists = Equipment.objects.get(pk=equip_id)
    form = AddEquipmentForm(request.POST or None, instance=equip_lists)
    if form.is_valid():
        form.save()
        return redirect('main_app:equip_list')
    context = {
        'form': form,
    }
    return render(request, 'main/edit_equip_list.html', context)


def delete_equip_list(request, equip_id):
    equip_lists = Equipment.objects.get(pk=equip_id)
    equip_lists.delete()
    return redirect('main_app:equip_list')


def research_cent(request):
    research_centres = ResearchCentres.objects.all()

    if request.method == "POST":
        form = AddResearchCentreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main_app:research_cent')
    else:
        form = AddResearchCentreForm

    context = {
        'research_centres': research_centres,
        'form': form,
    }
    return render(request, 'main/research_cent.html', context)


def edit_research_cent(request, centre_id):
    centres = ResearchCentres.objects.get(pk=centre_id)
    form = AddResearchCentreForm(request.POST or None, instance=centres)
    if form.is_valid():
        form.save()
        return redirect('main_app:research_cent')
    context = {
        'form': form,
    }
    return render(request, 'main/edit_research_cent.html', context)


def delete_research_cent(request, centre_id):
    centres = ResearchCentres.objects.get(pk=centre_id)
    centres.delete()
    return redirect('main_app:research_cent')


def group(request):
    groups = Group.objects.all()

    if request.method == "POST":
        form = AddGroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main_app:group')
    else:
        form = AddGroupForm

    context = {
        'groups': groups,
        'form': form,
    }
    return render(request, 'main/group.html', context)


def edit_group(request, group_id):
    groups = Group.objects.get(pk=group_id)
    form = AddGroupForm(request.POST or None, instance=groups)
    if form.is_valid():
        form.save()
        return redirect('main_app:group')
    context = {
        'form': form,
    }
    return render(request, 'main/edit_group.html', context)


def delete_group(request, group_id):
    groups = Group.objects.get(pk=group_id)
    groups.delete()
    return redirect('main_app:group')


def booking(request):
    bookings = Booking.objects.all()

    if request.method == "POST":
        form = AddBookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main_app:home')
    else:
        status = {'status': 'Pending'}
        form = AddBookingForm(initial=status)

    context = {
        'bookings': bookings,
        'form': form,
    }
    return render(request, 'main/booking.html', context)


def edit_booking(request, booking_id):
    bookings = Booking.objects.get(pk=booking_id)
    form = AddBookingForm(request.POST or None, instance=bookings)
    if form.is_valid():
        form.save()
        return redirect('main_app:home')
    context = {
        'form': form,
    }
    return render(request, 'main/edit_booking.html', context)


def delete_booking(request, booking_id):
    bookings = Booking.objects.get(pk=booking_id)
    bookings.delete()
    return redirect('main_app:home')


def status_choice(request):
    status = StatusChoice.objects.all()

    if request.method == "POST":
        form = StatusChoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main_app:status_choice')
    else:
        form = StatusChoiceForm

    context = {
        'status': status,
        'form': form,
    }
    return render(request, 'main/status_choice.html', context)


def edit_status_choice(request, status_id):
    status = StatusChoice.objects.get(pk=status_id)
    form = StatusChoiceForm(request.POST or None, instance=status)
    if form.is_valid():
        form.save()
        return redirect('main_app:status_choice')
    context = {
        'form': form,
    }
    return render(request, 'main/edit_status_choice.html', context)


def delete_status_choice(request, status_id):
    status = StatusChoice.objects.get(pk=status_id)
    status.delete()
    return redirect('main_app:status_choice')


class booking_calendar(generic.ListView):
    model = Booking
    template_name = 'main/booking_calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        room_name = self.kwargs['room_name']
        room = get_object_or_404(Rooms, room_name=room_name)
        context['calendar_title'] = room.room_name
        #bookings = room.booking_set.all()
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month, room_name)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        context['room'] = room.room_name
        #context['bookings'] = bookings

        return context


def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()


def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month


def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month


def get_rooms(request):
    building_id = request.GET.get('building_id')
    rooms = Rooms.objects.filter(building_id=building_id)
    data = [{'id': room.id, 'name': room.room_name} for room in rooms]
    return JsonResponse(data, safe=False)


def get_equipments(request):
    room_id = request.GET.get('room_id')
    building_id = request.GET.get('building_id')
    equipments = Equipment.objects.filter(Q(room_id=room_id) & Q(building_id=building_id))
    data = [{'id': equipment.id, 'name': equipment.equip_name} for equipment in equipments]
    return JsonResponse(data, safe=False)











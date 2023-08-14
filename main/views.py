from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Q
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.models import Group
from django.contrib import messages
from django.forms import formset_factory
import json
from django.http import JsonResponse


from django.utils.safestring import mark_safe
import calendar
from django.views import generic
from django.utils import timezone
from datetime import datetime, timedelta, date

from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader




from .models import Building, BuildingLevel, Rooms, Equipment,\
    ResearchCentres,  Booking, StatusChoice, AppUser, Project, ResearchGroup,PrestartCheck, EquipmentGroup
from .forms import AddBuildingForm, AddBuildingLevelForm, AddBuildingRoomForm, AddEquipmentForm, AddResearchCentreForm, \
     AddBookingForm, EditBookingForm, StatusChoiceForm, AddUserForm, AddProjectForm, AddGroupForm,\
    AddEquipGroupForm

from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users

from .utils import Calendar
# Create your views here.


# @unauthenticated_user
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('main_app:home')
        else:
            messages.info(request, 'Username or password is incorrect')
    context = {}
    return render(request, 'main/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('main_app:login')


@login_required(login_url='main_app:login')
def home(request):
    login_user = request.user.username
    app_user = AppUser.objects.get(user_name=request.user)
    if request.user.groups.filter(name='Coordinator').exists():
        bookings = Booking.objects.all().order_by('-start_date')
    else:
        try:
            user = AppUser.objects.get(user_name=request.user)  # Get the AppUser object of the logged-in user
            bookings = Booking.objects.filter(user_name=user).exclude(status='Cancelled').order_by('start_date')
        except AppUser.DoesNotExist:
            # Handle the case when the logged-in user doesn't have an associated AppUser object
            bookings = Booking.objects.none()

    context = {
        'bookings': bookings,
        'login_user': login_user,
        'app_user': app_user,

    }
    return render(request, 'main/home.html', context)


@login_required(login_url='main_app:login')
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


@login_required(login_url='main_app:login')
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


@login_required(login_url='main_app:login')
def delete_building_list(request, building_id):
    build_lists = Building.objects.get(pk=building_id)
    build_lists.delete()
    return redirect('main_app:building_list')


@login_required(login_url='main_app:login')
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

@login_required(login_url='main_app:login')
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

@login_required(login_url='main_app:login')
def delete_build_level(request, level_id):
    build_levels = BuildingLevel.objects.get(pk=level_id)
    build_levels.delete()
    return redirect('main_app:build_level')

@login_required(login_url='main_app:login')
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

@login_required(login_url='main_app:login')
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

@login_required(login_url='main_app:login')
def delete_build_room(request, room_id):
    build_levels = Rooms.objects.get(pk=room_id)
    build_levels.delete()
    return redirect('main_app:build_room')

@login_required(login_url='main_app:login')
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

@login_required(login_url='main_app:login')
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


@login_required(login_url='main_app:login')
def delete_equip_list(request, equip_id):
    equip_lists = Equipment.objects.get(pk=equip_id)
    equip_lists.delete()
    return redirect('main_app:equip_list')


@login_required(login_url='main_app:login')
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


@login_required(login_url='main_app:login')
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


@login_required(login_url='main_app:login')
def delete_research_cent(request, centre_id):
    centres = ResearchCentres.objects.get(pk=centre_id)
    centres.delete()
    return redirect('main_app:research_cent')


@login_required(login_url='main_app:login')
def group(request):
    groups = ResearchGroup.objects.all()

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


@login_required(login_url='main_app:login')
def edit_group(request, group_id):
    groups = ResearchGroup.objects.get(pk=group_id)
    form = AddGroupForm(request.POST or None, instance=groups)
    if form.is_valid():
        form.save()
        return redirect('main_app:group')
    context = {
        'form': form,
    }
    return render(request, 'main/edit_group.html', context)


@login_required(login_url='main_app:login')
def delete_group(request, group_id):
    groups = ResearchGroup.objects.get(pk=group_id)
    groups.delete()
    return redirect('main_app:group')


@login_required(login_url='main_app:login')
def booking(request):
    try:
        app_user = AppUser.objects.get(user_name=request.user)
    except AppUser.DoesNotExist:
        return redirect('main_app:home')
    if request.method == "POST":
        form = AddBookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main_app:home')
    else:
        status = 'Approved'
        #form = AddBookingForm(initial=status)
        form = AddBookingForm(initial={'user_name': app_user, 'status': status})

    context = {
        'form': form,
    }
    return render(request, 'main/booking.html', context)


@login_required(login_url='main_app:login')
def edit_booking(request, booking_id):
    bookings = Booking.objects.get(pk=booking_id)
    initial_data = {
        'group': bookings.proj_data.group if bookings.proj_data else None,
        'building': bookings.equip_name.building if bookings.equip_name else None,
        'room': bookings.equip_name.room if bookings.equip_name else None,
    }
    form = EditBookingForm(request.POST or None, instance=bookings, initial=initial_data)
    if form.is_valid():
        form.save()
        return redirect('main_app:home')
    context = {
        'form': form,
    }
    return render(request, 'main/edit_booking.html', context)


@login_required(login_url='main_app:login')
def delete_booking(request, booking_id):
    bookings = Booking.objects.get(pk=booking_id)
    bookings.delete()
    return redirect('main_app:home')


@login_required(login_url='main_app:login')
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


@login_required(login_url='main_app:login')
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


@login_required(login_url='main_app:login')
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


def get_projects(request):
    group_id = request.GET.get('group_id')
    projects = Project.objects.filter(group_id=group_id)
    data = [{'id': project.id, 'name': project.proj_concat} for project in projects]
    return JsonResponse(data, safe=False)


@login_required(login_url='main_app:login')
def add_user(request):
    addusers = AppUser.objects.all().order_by('centre__name', 'group__name')

    if request.method == "POST":
        form = AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main_app:add_user')
    else:
        form = AddUserForm()

    context = {
        'addusers': addusers,
        'form': form,
    }
    return render(request, 'main/add_user.html', context)


@login_required(login_url='main_app:login')
def edit_add_user(request, user_id):
    user = AppUser.objects.get(pk=user_id)
    form = AddUserForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        return redirect('main_app:add_user')
    context = {
        'form': form,
    }
    return render(request, 'main/edit_add_user.html', context)


@login_required(login_url='main_app:login')
def delete_add_user(request, user_id):
    user = AppUser.objects.get(pk=user_id)
    user.delete()
    return redirect('main_app:add_user')


@login_required(login_url='main_app:login')
def add_project(request):
    projects = Project.objects.all()

    if request.method == "POST":
        form = AddProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main_app:add_project')
    else:
        form = AddProjectForm()

    context = {
        'projects': projects,
        'form': form,
    }
    return render(request, 'main/add_project.html', context)


@login_required(login_url='main_app:login')
def edit_add_project(request, project_id):
    projects = Project.objects.get(pk=project_id)
    form = AddProjectForm(request.POST or None, instance=projects)
    if form.is_valid():
        form.save()
        return redirect('main_app:add_project')
    context = {
        'form': form,
    }
    return render(request, 'main/edit_add_project.html', context)


@login_required(login_url='main_app:login')
def delete_add_project(request, project_id):
    project = Project.objects.get(pk=project_id)
    project.delete()
    return redirect('main_app:add_project')


@login_required(login_url='main_app:login')
def add_equip_group(request):
    groups = EquipmentGroup.objects.all()

    if request.method == "POST":
        form = AddEquipGroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main_app:add_equip_group')
    else:
        form = AddEquipGroupForm()

    context = {
        'groups': groups,
        'form': form,
    }
    return render(request, 'main/add_equip_group.html', context)


@login_required(login_url='main_app:login')
def monthly_report_form(request):
    return render(request, 'main/monthly_report_form.html')


@login_required(login_url='main_app:login')
def generate_monthly_report(request):
    month = request.GET.get('month')
    year = request.GET.get('year')
    month_name = calendar.month_name[int(month)]

    #find first day of month
    start_date= datetime.strptime(f"{year}-{month}-01","%Y-%m-%d").date()

    #find last day of month
    if month == '12':
        end_date = datetime.strptime(f"{int(year)+1}-01-01", "%Y-%m-%d").date()
    else:
        end_date = datetime.strptime(f"{year}-{int(month)+1}-01", "%Y-%m-%d").date()

    filename = f'monthly_report_{month}_{year}.pdf'
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'

    canv = canvas.Canvas(response, pagesize=A4)

    #draw logo to report
    img_path = "static/main/images/uq-logo.png"
    img = ImageReader(img_path)
    img_width, img_height = img.getSize()
    canv.drawImage(img, 0, A4[1] - img_height, width=img_width, height=img_height)


    num_bookings = Booking.objects.filter(request_date__gte=start_date, request_date__lt=end_date).count()


    #Title Section
    canv.setFillColorRGB(255, 255, 255)
    canv.setStrokeColorRGB(0.5, 0.5, 0.5)
    margin = 20
    title_rect_height = img_height
    title_rect_y = 715
    title_rect_width = A4[0] - 2 * margin
    title_text = f"Laboratory Monthly Report for {month_name} {year}"
    canv.rect(margin, title_rect_y, title_rect_width, title_rect_height, stroke=1, fill=1)
    canv.setFillColorRGB(0, 0, 0)
    #canv.setFont('Helvetica-Bold', 20)
    title_text_width = canv.stringWidth(title_text, 'Helvetica-Bold', 20)
    title_x = A4[0] - margin - title_text_width# Calculate the x-coordinate
    canv.drawString(title_x, title_rect_y + 15, title_text)  # Use calculated x-coordinate


    #Body Section
    canv.setFont("Helvetica", 12)  # set font size back to 12
    canv.drawString(50, 660, f"This report provides a summary analysis of the SMI Indooroopilly Laboratory")
    canv.drawString(50, 640, f"The number of equipment bookings for the month was: {num_bookings}")


    canv.save()
    return response







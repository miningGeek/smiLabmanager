from django import forms
from django.forms import ModelForm, DateField, widgets

from .models import Building, BuildingLevel, Rooms, Equipment,\
    ResearchCentres, Group, Booking, AppUser, StatusChoice, Project


class AddBuildingForm(ModelForm):
    class Meta:
        model = Building
        fields = (
            'building_name',
        )
        widgets = {
            'building_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Required'}),
        }


class AddBuildingLevelForm(ModelForm):
    class Meta:
        model = BuildingLevel
        fields = (
            'level_name',
        )
        widgets = {
            'level_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Required'}),
        }


class AddBuildingRoomForm(ModelForm):
    building_level = forms.ModelChoiceField(queryset=BuildingLevel.objects.all(), empty_label="Select Building Level")
    building = forms.ModelChoiceField(queryset=Building.objects.all(), empty_label="Select Building")

    class Meta:
        model = Rooms
        fields = (
            'room_number',
            'room_name',
            'building',
            'building_level',
        )
        widgets = {
            'room_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Required'}),
            'room_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Required'}),
        }


class AddEquipmentForm(ModelForm):
    room = forms.ModelChoiceField(queryset=Rooms.objects.all(), empty_label="Select Room")
    building_level = forms.ModelChoiceField(queryset=BuildingLevel.objects.all(), empty_label="Select Building Level")
    building = forms.ModelChoiceField(queryset=Building.objects.all(), empty_label="Select Building")

    class Meta:
        model = Equipment
        fields = (
            'equip_name',
            'building',
            'building_level',
            'room',
            'description',
        )
        widgets = {
            'equip_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Required'}),
        }


class AddResearchCentreForm(ModelForm):
    class Meta:
        model = ResearchCentres
        fields = (
            'name',
        )
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Required'}),
        }


class AddGroupForm(ModelForm):
    centres = forms.ModelChoiceField(queryset=ResearchCentres.objects.all())

    class Meta:
        model = Group
        fields = (
            'name',
            'centres',
            'status_active',

        )
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Required'}),
        }


from django.forms import ModelForm, widgets
from django import forms
from .models import Booking, Group, Equipment, StatusChoice


class AddBookingForm(ModelForm):
    group = forms.ModelChoiceField(queryset=Group.objects.all())
    equip_name = forms.ModelChoiceField(queryset=Equipment.objects.all())
    room = forms.ModelChoiceField(queryset=Rooms.objects.all())
    building = forms.ModelChoiceField(queryset=Building.objects.all())

    class Meta:
        model = Booking
        fields = (
            'user_name',
            'proj_data',
            'group',
            'building',
            'room',
            'equip_name',
            'start_date',
            'shift',
            'num_hours',
            'status',

        )
        labels = {
            'user_name': 'User Name',
            'proj_data': 'Project Info',
            'group': 'Group',
            'building': 'Building',
            'room': 'Room',
            'equip_name': 'Equipment',
            'start_date': 'Date required',
            'shift': 'Shift',
            'num_hours': 'Hours Expected',
            'status': 'Status',

        }
        widgets = {

            'start_date': widgets.DateInput(attrs={'type': 'date', 'class': 'short-field'}),
            'status': widgets.TextInput(attrs={'disabled': 'disabled', 'initial': 'Approved'}),

        }

class AddBookingForm(ModelForm):
    group = forms.ModelChoiceField(queryset=Group.objects.all())
    equip_name = forms.ModelChoiceField(queryset=Equipment.objects.all())
    room = forms.ModelChoiceField(queryset=Rooms.objects.all())
    building = forms.ModelChoiceField(queryset=Building.objects.all())

    class Meta:
        model = Booking
        fields = (
            'user_name',
            'proj_data',
            'group',
            'building',
            'room',
            'equip_name',
            'start_date',
            'shift',
            'num_hours',
            'status',

        )
        labels = {
            'user_name': 'User Name',
            'proj_data': 'Project Info',
            'group': 'Group',
            'building': 'Building',
            'room': 'Room',
            'equip_name': 'Equipment',
            'start_date': 'Date required',
            'shift': 'Shift',
            'num_hours': 'Hours Expected',
            'status': 'Status',

        }
        widgets = {

            'start_date': widgets.DateInput(attrs={'type': 'date', 'class': 'short-field'}),
            'status': widgets.TextInput(attrs={'disabled': 'disabled', 'initial': 'Pending'}),

        }

class EditBookingForm(ModelForm):
    group = forms.ModelChoiceField(queryset=Group.objects.all())
    equip_name = forms.ModelChoiceField(queryset=Equipment.objects.all())
    building = forms.ModelChoiceField(queryset=Building.objects.all(), required=False)
    room = forms.ModelChoiceField(queryset=Rooms.objects.all(), required=False)

    class Meta:
        model = Booking
        fields = (
            'user_name',
            'proj_data',
            'group',
            'building',
            'room',
            'equip_name',
            'start_date',
            'shift',
            'num_hours',
            'status',

        )
        labels = {
            'user_name': 'User Name',
            'proj_data': 'Project Info',
            'group': 'Group',
            'building': 'Building',
            'room': 'Room',
            'equip_name': 'Equipment',
            'start_date': 'Date required',
            'shift': 'Shift',
            'num_hours': 'Hours Expected',
            'status': 'Status',

        }
        widgets = {

            'start_date': widgets.DateInput(attrs={'type': 'date', 'class': 'short-field'}),


        }



class StatusChoiceForm(ModelForm):
    class Meta:
        model = StatusChoice
        fields = (
            'status',
        )
        widgets = {
            'status': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Required'}),
        }


class AddUserForm(ModelForm):
    class Meta:
        model = AppUser
        fields = (
            'user_name',
            'first_name',
            'centre',
            'group',
            'status_active',
        )
        labels = {
            'user_name': 'User Name',
            'first_name': 'First Name',
            'centre': 'Research Centre',
            'group': 'Group',
            'status_active': 'Active',

        }


class AddProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = (
            'proj_number',
            'ciloxis_num',
        )
        labels = {
            'proj_number': 'Project Number',
            'ciloxis_num': 'Ciloxis Number',
        }
from django import forms
from django.forms import ModelForm, DateField, widgets

from .models import Building, BuildingLevel, Rooms, Equipment,\
    ResearchCentres, Group, Booking, User, StatusChoice


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
            'group',
            'building',
            'room',
            'equip_name',
            'start_date',
            'shift',
            'status',
        )
        labels = {
            'user_name': 'User Name',
            'group': 'Group',
            'building': 'Building',
            'room': 'Room',
            'equip_name': 'Equipment',
            'start_date': 'Start Date',
            'shift': 'Shift',
            'status': 'Status',
        }
        widgets = {

            'start_date': widgets.DateInput(attrs={'type': 'date', 'class': 'short-field'}),
            'status': widgets.TextInput(attrs={'disabled': 'disabled', 'initial': 'Pending'}),
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

from django import forms
from django.forms import ModelForm, DateField, widgets

from .models import Building, BuildingLevel, Rooms, Equipment,\
    ResearchCentres,ResearchGroup, Booking, AppUser, StatusChoice, Project,PrestartCheck, EquipmentGroup


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
    equip_group = forms.ModelChoiceField(queryset=EquipmentGroup.objects.all(),empty_label='Select Equipment Group')
    class Meta:
        model = Equipment
        fields = (
            'equip_name',
            'building',
            'building_level',
            'room',
            'description',
            'group_owner',
            'is_equip',
            'equip_group',

        )
        widgets = {
            'equip_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Required'}),
        }


class AddEquipGroupForm(ModelForm):
    class Meta:
        model = EquipmentGroup
        fields = (
            'equip_group',

        )
        widgets = {
            'building_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Required'}),
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
        model = ResearchGroup
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
from .models import Booking, Equipment, StatusChoice


class AddBookingForm(ModelForm):

    group = forms.ModelChoiceField(queryset=ResearchGroup.objects.all())
    proj_data = forms.ModelChoiceField(queryset=Project.objects.all())
    equip_name = forms.ModelChoiceField(queryset=Equipment.objects.all())
    room = forms.ModelChoiceField(queryset=Rooms.objects.all())
    building = forms.ModelChoiceField(queryset=Building.objects.all())

    class Meta:
        model = Booking
        fields = (
            'user_name',
            'group',
            'proj_data',
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
            'group': 'Group',
            'proj_data': 'Project Info',
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




class EditBookingForm(ModelForm):
    group = forms.ModelChoiceField(queryset=ResearchGroup.objects.all())
    equip_name = forms.ModelChoiceField(queryset=Equipment.objects.all())
    building = forms.ModelChoiceField(queryset=Building.objects.all(), required=True)
    room = forms.ModelChoiceField(queryset=Rooms.objects.all(), required=True)

    class Meta:
        model = Booking
        fields = (
            'user_name',
            'group',
            'proj_data',
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
            'group': 'Group',
            'proj_data': 'Project Info',
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
            'ute_auth',
        )
        labels = {
            'user_name': 'User Name',
            'first_name': 'First Name',
            'centre': 'Research Centre',
            'group': 'Group',
            'status_active': 'Active',
            'ute_auth': 'Authorised Ute Use',

        }


class AddProjectForm(ModelForm):
    group = forms.ModelChoiceField(queryset=ResearchGroup.objects.all())

    class Meta:
        model = Project
        fields = (
            'proj_number',
            'ciloxis_num',
            'group'
        )
        labels = {
            'proj_number': 'Project Number',
            'ciloxis_num': 'Ciloxis Number',
            'group': 'Group',
        }

# class AddRotapPrestartForm(ModelForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         # Filter the 'equip_name' field queryset based on equip_group name
#         filtered_equip_names = Equipment.objects.filter(equip_group__equip_group__iexact='Rotap')
#         self.fields['equip_name'].queryset = filtered_equip_names
#     class Meta:
#         model = PrestartCheck
#         fields = (
#             'username',
#             'equip_name',
#             'trained',
#             'sop_ra',
#             'test_tag',
#             'elect_lead',
#             'stop_button',
#             'guarding',
#             'dust_extract',
#             'comments',
#         )
#         labels = {
#             'username': 'Select User',
#             'equip_name': 'Select Equipment',
#             'trained': 'Trained & Competent',
#             'sop_ra': 'Read SWM & RA',
#             'test_tag': 'Test & Tag in date',
#             'elect_lead': 'Electrical lead damaged',
#             'stop_button': 'Stop button working',
#             'guarding': 'Guarding in place',
#             'dust_extract': 'Dust Extract on',
#             'comments': 'Any Comments',
#
#         }
#         widgets = {
#             'prestart_date': widgets.DateInput(attrs={'disabled': 'disabled'}),
#         }

# class AddSplitterLargePrestartForm(ModelForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         # Filter the 'equip_name' field queryset based on equip_group name
#         filtered_equip_names = Equipment.objects.filter(equip_group__equip_group__iexact='Large-Splitter')
#         self.fields['equip_name'].queryset = filtered_equip_names
#     class Meta:
#         model = PrestartCheck
#         fields = (
#             'username',
#             'equip_name',
#             'trained',
#             'sop_ra',
#             'test_tag',
#             'elect_lead',
#             'stop_button',
#             'guarding',
#             'interlock',
#             'dust_extract',
#             'comments',
#         )
#         labels = {
#             'username': 'Select User',
#             'equip_name': 'Select Equipment',
#             'trained': 'Trained & Competent',
#             'sop_ra': 'Read SWM & RA',
#             'test_tag': 'Test & Tag in date',
#             'elect_lead': 'Electrical lead damaged',
#             'stop_button': 'Stop button working',
#             'guarding': 'Guarding in place',
#             'interlock': 'Interlocks are working',
#             'dust_extract': 'Dust Extract on',
#             'comments': 'Any Comments',
#
#         }
#         widgets = {
#             'prestart_date': widgets.DateInput(attrs={'disabled': 'disabled'}),
#         }
#
#
# class AddSmallJawPrestartForm(ModelForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         # Filter the 'equip_name' field queryset based on equip_group name
#         filtered_equip_names = Equipment.objects.filter(equip_group__equip_group__iexact='Small-Jaw')
#         self.fields['equip_name'].queryset = filtered_equip_names
#     class Meta:
#         model = PrestartCheck
#         fields = (
#             'username',
#             'equip_name',
#             'trained',
#             'sop_ra',
#             'test_tag',
#             'elect_lead',
#             'stop_button',
#             'guarding',
#             'dust_extract',
#             'comments',
#         )
#         labels = {
#             'username': 'Select User',
#             'equip_name': 'Select Equipment',
#             'trained': 'Trained & Competent',
#             'sop_ra': 'Read SWM & RA',
#             'test_tag': 'Test & Tag in date',
#             'elect_lead': 'Electrical lead damaged',
#             'stop_button': 'Stop button working',
#             'guarding': 'Guarding in place',
#             'dust_extract': 'Dust Extract on',
#             'comments': 'Any Comments',
#
#         }
#         widgets = {
#             'prestart_date': widgets.DateInput(attrs={'disabled': 'disabled'}),
#         }
#
# class AddFilterPressPrestartForm(ModelForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         # Filter the 'equip_name' field queryset based on equip_group name
#         filtered_equip_names = Equipment.objects.filter(equip_group__equip_group__iexact='Filter-Pots')
#         self.fields['equip_name'].queryset = filtered_equip_names
#     class Meta:
#         model = PrestartCheck
#         fields = (
#             'username',
#             'equip_name',
#             'trained',
#             'sop_ra',
#             'air_pressure',
#             'noise_baffles',
#             'seals',
#             'filter_mat',
#             'anti_slip',
#             'comments',
#         )
#         labels = {
#             'username': 'Select User',
#             'equip_name': 'Select Equipment',
#             'trained': 'Trained & Competent',
#             'sop_ra': 'Read SWM & RA',
#             'air_pressure': 'Air Pressure <500kpa',
#             'noise_baffles': 'Noise Baffles Installed',
#             'seals': 'Rubber seals fitted & good condition',
#             'filter_mat': 'Filter Mat in good condition',
#             'anti_slip': 'Anti Slip mat fitted',
#             'comments': 'Any Comments',
#
#         }
#         widgets = {
#             'prestart_date': widgets.DateInput(attrs={'disabled': 'disabled'}),
#         }
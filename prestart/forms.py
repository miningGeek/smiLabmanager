from django import forms
from django.forms import ModelForm, DateField, widgets, ModelChoiceField

from main.models import PrestartCheck, Equipment, EquipmentGroup, AppUser


class AddRotapPrestartForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filter the 'equip_name' field queryset based on equip_group name
        filtered_equip_names = Equipment.objects.filter(equip_group__equip_group__iexact='Rotap')
        self.fields['equip_name'].queryset = filtered_equip_names
    class Meta:
        model = PrestartCheck
        fields = (
            'username',
            'equip_name',
            'trained',
            'sop_ra',
            'test_tag',
            'elect_lead',
            'stop_button',
            'guarding',
            'dust_extract',
            'comments',
        )
        labels = {
            'username': 'Select User',
            'equip_name': 'Select Equipment',
            'trained': 'Trained & Competent',
            'sop_ra': 'Read SWM & RA',
            'test_tag': 'Test & Tag in date',
            'elect_lead': 'Electrical lead damaged',
            'stop_button': 'Stop button working',
            'guarding': 'Guarding in place',
            'dust_extract': 'Dust Extract on',
            'comments': 'Any Comments',

        }
        widgets = {
            'prestart_date': widgets.DateInput(attrs={'disabled': 'disabled'}),
        }

class AddSplitterLargePrestartForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filter the 'equip_name' field queryset based on equip_group name
        filtered_equip_names = Equipment.objects.filter(equip_group__equip_group__iexact='Large-Splitter')
        self.fields['equip_name'].queryset = filtered_equip_names
    class Meta:
        model = PrestartCheck
        fields = (
            'username',
            'equip_name',
            'trained',
            'sop_ra',
            'test_tag',
            'elect_lead',
            'stop_button',
            'guarding',
            'interlock',
            'dust_extract',
            'comments',
        )
        labels = {
            'username': 'Select User',
            'equip_name': 'Select Equipment',
            'trained': 'Trained & Competent',
            'sop_ra': 'Read SWM & RA',
            'test_tag': 'Test & Tag in date',
            'elect_lead': 'Electrical lead damaged',
            'stop_button': 'Stop button working',
            'guarding': 'Guarding in place',
            'interlock': 'Interlocks are working',
            'dust_extract': 'Dust Extract on',
            'comments': 'Any Comments',

        }
        widgets = {
            'prestart_date': widgets.DateInput(attrs={'disabled': 'disabled'}),
        }


class AddSmallJawPrestartForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filter the 'equip_name' field queryset based on equip_group name
        filtered_equip_names = Equipment.objects.filter(equip_group__equip_group__iexact='Small-Jaw')
        self.fields['equip_name'].queryset = filtered_equip_names
    class Meta:
        model = PrestartCheck
        fields = (
            'username',
            'equip_name',
            'trained',
            'sop_ra',
            'test_tag',
            'elect_lead',
            'stop_button',
            'guarding',
            'dust_extract',
            'comments',
        )
        labels = {
            'username': 'Select User',
            'equip_name': 'Select Equipment',
            'trained': 'Trained & Competent',
            'sop_ra': 'Read SWM & RA',
            'test_tag': 'Test & Tag in date',
            'elect_lead': 'Electrical lead damaged',
            'stop_button': 'Stop button working',
            'guarding': 'Guarding in place',
            'dust_extract': 'Dust Extract on',
            'comments': 'Any Comments',

        }
        widgets = {
            'prestart_date': widgets.DateInput(attrs={'disabled': 'disabled'}),
        }

class AddFilterPressPrestartForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filter the 'equip_name' field queryset based on equip_group name
        filtered_equip_names = Equipment.objects.filter(equip_group__equip_group__iexact='Filter-Pots')
        self.fields['equip_name'].queryset = filtered_equip_names
    class Meta:
        model = PrestartCheck
        fields = (
            'username',
            'equip_name',
            'trained',
            'sop_ra',
            'air_pressure',
            'noise_baffles',
            'seals',
            'filter_mat',
            'anti_slip',
            'comments',
        )
        labels = {
            'username': 'Select User',
            'equip_name': 'Select Equipment',
            'trained': 'Trained & Competent',
            'sop_ra': 'Read SWM & RA',
            'air_pressure': 'Air Pressure <500kpa',
            'noise_baffles': 'Noise Baffles Installed',
            'seals': 'Rubber seals fitted & good condition',
            'filter_mat': 'Filter Mat in good condition',
            'anti_slip': 'Anti Slip mat fitted',
            'comments': 'Any Comments',

        }
        widgets = {
            'prestart_date': widgets.DateInput(attrs={'disabled': 'disabled'}),
        }
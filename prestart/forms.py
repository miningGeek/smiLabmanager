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
            'elect_lead': 'Electrical lead undamaged',
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
            'elect_lead': 'Electrical lead undamaged',
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
            'elect_lead': 'Electrical lead undamaged',
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

class AddGilsonPrestartForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filter the 'equip_name' field queryset based on equip_group name
        filtered_equip_names = Equipment.objects.filter(equip_group__equip_group__iexact='Shaker')
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
            'hyd_pump',
            'dust_extract',
            'comments',
        )
        labels = {
            'username': 'Select User',
            'equip_name': 'Select Equipment',
            'trained': 'Trained & Competent',
            'sop_ra': 'Read SWM & RA',
            'test_tag': 'Test & Tag in date',
            'elect_lead': 'Electrical lead undamaged',
            'stop_button': 'Stop button working',
            'guarding': 'Guarding fitted & good condition',
            'hyd_pump': 'Hydraulic pump working',
            'dust_extract': 'Dust extraction fitted & on',
            'comments': 'Any Comments',

        }
        widgets = {
            'prestart_date': widgets.DateInput(attrs={'disabled': 'disabled'}),
        }


class AddWetSievePrestartForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filter the 'equip_name' field queryset based on equip_group name
        filtered_equip_names = Equipment.objects.filter(equip_group__equip_group__iexact='Wet-Sieve')
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
            'water_elect',
            'comments',
        )
        labels = {
            'username': 'Select User',
            'equip_name': 'Select Equipment',
            'trained': 'Trained & Competent',
            'sop_ra': 'Read SWM & RA',
            'test_tag': 'Test & Tag in date',
            'elect_lead': 'Electrical lead undamaged',
            'water_elect': 'Electrical components off bench, away from water',
            'comments': 'Any Comments',

        }
        widgets = {
            'prestart_date': widgets.DateInput(attrs={'disabled': 'disabled'}),
        }


class AddBallMillPrestartForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filter the 'equip_name' field queryset based on equip_group name
        filtered_equip_names = Equipment.objects.filter(equip_group__equip_group__iexact='Ball-Mill')
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
            'elect_lead': 'Electrical lead undamaged',
            'stop_button': 'Stop button working',
            'guarding': 'Guarding in place',
            'interlock': 'Interlock working',
            'dust_extract': 'Dust extraction fitted & on',
            'comments': 'Any Comments',

        }
        widgets = {
            'prestart_date': widgets.DateInput(attrs={'disabled': 'disabled'}),
        }


class AddGlassSplitterPrestartForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filter the 'equip_name' field queryset based on equip_group name
        filtered_equip_names = Equipment.objects.filter(equip_group__equip_group__iexact='Glass-Splitter')
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
            'guarding',
            'glass_bott',
            'dust_extract',
            'comments',
        )
        labels = {
            'username': 'Select User',
            'equip_name': 'Select Equipment',
            'trained': 'Trained & Competent',
            'sop_ra': 'Read SWM & RA',
            'test_tag': 'Test & Tag in date',
            'elect_lead': 'Electrical lead undamaged',
            'guarding': 'Guarding in place',
            'glass_bott': 'Glass bottles free from damage',
            'dust_extract': 'Dust extraction in place & working',
            'comments': 'Any Comments',

        }
        widgets = {
            'prestart_date': widgets.DateInput(attrs={'disabled': 'disabled'}),
        }


class AddDropWeightPrestartForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filter the 'equip_name' field queryset based on equip_group name
        filtered_equip_names = Equipment.objects.filter(equip_group__equip_group__iexact='DWT')
        self.fields['equip_name'].queryset = filtered_equip_names
    class Meta:
        model = PrestartCheck
        fields = (
            'username',
            'equip_name',
            'trained',
            'sop_ra',
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
            'guarding': 'Guarding in place',
            'interlock': 'Interlock working',
            'dust_extract': 'Dust extraction in place & working',
            'comments': 'Any Comments',

        }
        widgets = {
            'prestart_date': widgets.DateInput(attrs={'disabled': 'disabled'}),
        }


class AddWetMillPrestartForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filter the 'equip_name' field queryset based on equip_group name
        filtered_equip_names = Equipment.objects.filter(equip_group__equip_group__iexact='Wet-Mill')
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
            'comments',
        )
        labels = {
            'username': 'Select User',
            'equip_name': 'Select Equipment',
            'trained': 'Trained & Competent',
            'sop_ra': 'Read SWM & RA',
            'test_tag': "Test & Tag current",
            'elect_lead': 'Electrical lead free from damage',
            'stop_button': 'Stop Button Working',
            'guarding': 'Guarding fitted & good condition',
            'interlock': 'Interlock working',
            'comments': 'Any Comments',

        }
        widgets = {
            'prestart_date': widgets.DateInput(attrs={'disabled': 'disabled'}),
        }


class AddSonicBathPrestartForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filter the 'equip_name' field queryset based on equip_group name
        filtered_equip_names = Equipment.objects.filter(equip_group__equip_group__iexact='Sonic')
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
            'water_elect',
            'water_level',
            'comments',
        )
        labels = {
            'username': 'Select User',
            'equip_name': 'Select Equipment',
            'trained': 'Trained & Competent',
            'sop_ra': 'Read SWM & RA',
            'test_tag': "Test & Tag current",
            'elect_lead': 'Electrical lead free from damage',
            'water_elect': 'Electrical lead away from water',
            'water_level': 'Water level filled to 2/3 level',
            'comments': 'Any Comments',

        }
        widgets = {
            'prestart_date': widgets.DateInput(attrs={'disabled': 'disabled'}),
        }


class AddPulveriserPrestartForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filter the 'equip_name' field queryset based on equip_group name
        filtered_equip_names = Equipment.objects.filter(equip_group__equip_group__iexact='Pulveriser')
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
            'guarding',
            'comments',
        )
        labels = {
            'username': 'Select User',
            'equip_name': 'Select Equipment',
            'trained': 'Trained & Competent',
            'sop_ra': 'Read SWM & RA',
            'test_tag': "Test & Tag current",
            'elect_lead': 'Electrical lead free from damage',
            'guarding': 'Guarding fitted & good condition',
            'comments': 'Any Comments',

        }
        widgets = {
            'prestart_date': widgets.DateInput(attrs={'disabled': 'disabled'}),
        }


class AddLargeCrusherPrestartForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filter the 'equip_name' field queryset based on equip_group name
        filtered_equip_names = Equipment.objects.filter(equip_group__equip_group__iexact='Crusher')
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
            'guarding',
            'hyd_oil_level',
            'dust_extract',
            'comments',
        )
        labels = {
            'username': 'Select User',
            'equip_name': 'Select Equipment',
            'trained': 'Trained & Competent',
            'sop_ra': 'Read SWM & RA',
            'test_tag': "Test & Tag current",
            'elect_lead': 'Electrical lead free from damage',
            'guarding': 'Guarding fitted & good condition',
            'hyd_oil_level': 'Hydraulic Oil level ok',
            'dust_extract': 'Dust extraction fitted & working',
            'comments': 'Any Comments',

        }
        widgets = {
            'prestart_date': widgets.DateInput(attrs={'disabled': 'disabled'}),
        }


class AddGoldConcPrestartForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filter the 'equip_name' field queryset based on equip_group name
        filtered_equip_names = Equipment.objects.filter(equip_group__equip_group__iexact='Gold-Conc')
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
            'comments',
        )
        labels = {
            'username': 'Select User',
            'equip_name': 'Select Equipment',
            'trained': 'Trained & Competent',
            'sop_ra': 'Read SWM & RA',
            'test_tag': "Test & Tag current",
            'elect_lead': 'Electrical lead free from damage',
            'comments': 'Any Comments',

        }
        widgets = {
            'prestart_date': widgets.DateInput(attrs={'disabled': 'disabled'}),
        }

class AddVacuumFilterPrestartForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filter the 'equip_name' field queryset based on equip_group name
        filtered_equip_names = Equipment.objects.filter(equip_group__equip_group__iexact='Vacuum_Filter')
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
            'water_elect',
            'glass_bott',
            'comments',
        )
        labels = {
            'username': 'Select User',
            'equip_name': 'Select Equipment',
            'trained': 'Trained & Competent',
            'sop_ra': 'Read SWM & RA',
            'test_tag': "Test & Tag current",
            'elect_lead': 'Electrical lead free from damage',
            'water_elect': 'Electrical lead clear of water',
            'glass_bott': 'Bucknor bottle empty & free of damage',
            'comments': 'Any Comments',

        }
        widgets = {
            'prestart_date': widgets.DateInput(attrs={'disabled': 'disabled'}),
        }


class AddFloatUnitPrestartForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filter the 'equip_name' field queryset based on equip_group name
        filtered_equip_names = Equipment.objects.filter(equip_group__equip_group__iexact='Flotation-Unit')
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
            'interlock',
            'air_pressure',
            'comments',
        )
        labels = {
            'username': 'Select User',
            'equip_name': 'Select Equipment',
            'trained': 'Trained & Competent',
            'sop_ra': 'Read SWM & RA',
            'test_tag': "Test & Tag current",
            'elect_lead': 'Electrical lead free from damage',
            'interlock': 'Interlock working',
            'air_pressure': 'Air pressure <200, airlines free of damage',
            'comments': 'Any Comments',

        }
        widgets = {
            'prestart_date': widgets.DateInput(attrs={'disabled': 'disabled'}),
        }


class AddFumeHoodPrestartForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filter the 'equip_name' field queryset based on equip_group name
        filtered_equip_names = Equipment.objects.filter(equip_group__equip_group__iexact='Fume-Hood')
        self.fields['equip_name'].queryset = filtered_equip_names
    class Meta:
        model = PrestartCheck
        fields = (
            'username',
            'equip_name',
            'trained',
            'sop_ra',
            'fume_filter',
            'dust_extract',
            'comments',
        )
        labels = {
            'username': 'Select User',
            'equip_name': 'Select Equipment',
            'trained': 'Trained & Competent',
            'sop_ra': 'Read SWM & RA',
            'fume_filter': 'Filter service current',
            'dust_extract': 'Extraction fan working',
            'comments': 'Any Comments',

        }
        widgets = {
            'prestart_date': widgets.DateInput(attrs={'disabled': 'disabled'}),
        }


class AddMixTankPrestartForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filter the 'equip_name' field queryset based on equip_group name
        filtered_equip_names = Equipment.objects.filter(equip_group__equip_group__iexact='Mixing-Tank')
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
            'water_elect',
            'comments',
        )
        labels = {
            'username': 'Select User',
            'equip_name': 'Select Equipment',
            'trained': 'Trained & Competent',
            'sop_ra': 'Read SWM & RA',
            'test_tag': 'Test & Tag current',
            'elect_lead': 'Electrical lead free of damage',
            'water_elect': 'Electrical lead clear of water',
            'comments': 'Any Comments',

        }
        widgets = {
            'prestart_date': widgets.DateInput(attrs={'disabled': 'disabled'}),
        }


class AddSizeAnalyserPrestartForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filter the 'equip_name' field queryset based on equip_group name
        filtered_equip_names = Equipment.objects.filter(equip_group__equip_group__iexact='Sizer-Analyser')
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
            'water_elect',
            'comments',
        )
        labels = {
            'username': 'Select User',
            'equip_name': 'Select Equipment',
            'trained': 'Trained & Competent',
            'sop_ra': 'Read SWM & RA',
            'test_tag': 'Test & Tag current',
            'elect_lead': 'Electrical lead free of damage',
            'water_elect': 'Electrical lead clear of water',
            'comments': 'Any Comments',

        }
        widgets = {
            'prestart_date': widgets.DateInput(attrs={'disabled': 'disabled'}),
        }


class AddCycloneRigPrestartForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filter the 'equip_name' field queryset based on equip_group name
        filtered_equip_names = Equipment.objects.filter(equip_group__equip_group__iexact='Cyclone-Rig')
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
            'water_elect',
            'comments',
        )
        labels = {
            'username': 'Select User',
            'equip_name': 'Select Equipment',
            'trained': 'Trained & Competent',
            'sop_ra': 'Read SWM & RA',
            'test_tag': 'Test & Tag current',
            'elect_lead': 'Electrical lead free of damage',
            'water_elect': 'Electrical lead clear of water',
            'comments': 'Any Comments',

        }
        widgets = {
            'prestart_date': widgets.DateInput(attrs={'disabled': 'disabled'}),
        }


class AddCycloneSizerPrestartForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filter the 'equip_name' field queryset based on equip_group name
        filtered_equip_names = Equipment.objects.filter(equip_group__equip_group__iexact='Cyclo-Sizer')
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
            'water_elect',
            'water_level',
            'glass_bott',
            'seals',
            'comments',
        )
        labels = {
            'username': 'Select User',
            'equip_name': 'Select Equipment',
            'trained': 'Trained & Competent',
            'sop_ra': 'Read SWM & RA',
            'test_tag': 'Test & Tag current',
            'elect_lead': 'Electrical lead free of damage',
            'water_elect': 'Electrical lead clear of water',
            'water_level': 'Water tap on, Tank full',
            'seals': 'No leakage from cyclones',
            'comments': 'Any Comments',

        }
        widgets = {
            'prestart_date': widgets.DateInput(attrs={'disabled': 'disabled'}),
        }

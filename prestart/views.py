from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required


from main.models import PrestartCheck, Equipment, EquipmentGroup, AppUser
from .forms import *

# Create your views here.

def pre_home(request):

    context = {

    }
    return render(request, 'prestart/pre_home.html', context)


@login_required(login_url='main_app:login')
def prestart_list(request):
    prestarts = PrestartCheck.objects.all()
    context ={
       'prestarts': prestarts
    }
    return render(request, 'prestart/prestart_list.html', context)



def pre_thank(request):
    context = {}
    return render(request, 'prestart/pre_thank.html', context)


def rotap_prestart(request):
    form = AddRotapPrestartForm(request.POST)

    # Filter the 'equip_name' field queryset based on your criteria
    # For example, let's say you want to show only certain equipment names
    filtered_equip_names = Equipment.objects.filter(equip_group__equip_group__iexact='Rotap')
    print(filtered_equip_names)
    form.fields['equip_name'].queryset = filtered_equip_names
    if form.is_valid():
        form.save()
        return redirect('prestart_app:pre_thank')
    else:
        form = AddRotapPrestartForm(use_required_attribute=False)
    context = {
        'form': form,
        }
    return render(request, 'prestart/rotap_prestart.html', context)


def large_splitter_prestart(request):
    form = AddSplitterLargePrestartForm(request.POST)

    # Filter the 'equip_name' field queryset based on your criteria
    # For example, let's say you want to show only certain equipment names
    filtered_equip_names = Equipment.objects.filter(equip_group__equip_group__iexact='Large-Splitter')
    print(filtered_equip_names)
    form.fields['equip_name'].queryset = filtered_equip_names
    if form.is_valid():
        form.save()
        return redirect('prestart_app:pre_thank')
    else:
        form = AddSplitterLargePrestartForm(use_required_attribute=False)
    context = {
        'form': form,
    }
    return render(request, 'prestart/large_splitter_prestart.html', context)


def small_jaw_prestart(request):
    form = AddSmallJawPrestartForm(request.POST)

    # Filter the 'equip_name' field queryset based on your criteria
    # For example, let's say you want to show only certain equipment names
    filtered_equip_names = Equipment.objects.filter(equip_group__equip_group__iexact='Small-Jaw')
    print(filtered_equip_names)
    form.fields['equip_name'].queryset = filtered_equip_names
    if form.is_valid():
        form.save()
        return redirect('prestart_app:pre_thank')
    else:
        form = AddSmallJawPrestartForm(use_required_attribute=False)
    context = {
        'form': form,
    }
    return render(request, 'prestart/small_jaw_prestart.html', context)


def filter_press_prestart(request):
    form = AddFilterPressPrestartForm(request.POST)

    # Filter the 'equip_name' field queryset based on your criteria
    # For example, let's say you want to show only certain equipment names
    filtered_equip_names = Equipment.objects.filter(equip_group__equip_group__iexact='Filter-Pots')
    print(filtered_equip_names)
    form.fields['equip_name'].queryset = filtered_equip_names
    if form.is_valid():
        form.save()
        return redirect('prestart_app:pre_thank')
    else:
        form = AddFilterPressPrestartForm(use_required_attribute=False)
    context = {
        'form': form,
    }
    return render(request, 'prestart/filter_press_prestart.html', context)


def gilson_prestart(request):
    form = AddGilsonPrestartForm(request.POST)

    # Filter the 'equip_name' field queryset based on your criteria
    # For example, let's say you want to show only certain equipment names
    filtered_equip_names = Equipment.objects.filter(equip_group__equip_group__iexact='Shaker')
    print(filtered_equip_names)
    form.fields['equip_name'].queryset = filtered_equip_names
    if form.is_valid():
        form.save()
        return redirect('prestart_app:pre_thank')
    else:
        form = AddGilsonPrestartForm(use_required_attribute=False)
    context = {
        'form': form,
    }
    return render(request, 'prestart/gilson_prestart.html', context)


def wet_sieve_prestart(request):
    form = AddWetSievePrestartForm(request.POST)

    # Filter the 'equip_name' field queryset based on your criteria
    # For example, let's say you want to show only certain equipment names
    filtered_equip_names = Equipment.objects.filter(equip_group__equip_group__iexact='Wet-Sieve')
    print(filtered_equip_names)
    form.fields['equip_name'].queryset = filtered_equip_names
    if form.is_valid():
        form.save()
        return redirect('prestart_app:pre_thank')
    else:
        form = AddWetSievePrestartForm(use_required_attribute=False)
    context = {
        'form': form,
    }
    return render(request, 'prestart/gilson_prestart.html', context)


def ball_mill_prestart(request):
    form = AddBallMillPrestartForm(request.POST)

    # Filter the 'equip_name' field queryset based on your criteria
    # For example, let's say you want to show only certain equipment names
    filtered_equip_names = Equipment.objects.filter(equip_group__equip_group__iexact='Ball-Mill')
    print(filtered_equip_names)
    form.fields['equip_name'].queryset = filtered_equip_names
    if form.is_valid():
        form.save()
        return redirect('prestart_app:pre_thank')
    else:
        form = AddBallMillPrestartForm(use_required_attribute=False)
    context = {
        'form': form,
    }
    return render(request, 'prestart/gilson_prestart.html', context)


def glass_splitter_prestart(request):
    form = AddGlassSplitterPrestartForm(request.POST)

    # Filter the 'equip_name' field queryset based on your criteria
    # For example, let's say you want to show only certain equipment names
    filtered_equip_names = Equipment.objects.filter(equip_group__equip_group__iexact='Glass-Splitter')
    print(filtered_equip_names)
    form.fields['equip_name'].queryset = filtered_equip_names
    if form.is_valid():
        form.save()
        return redirect('prestart_app:pre_thank')
    else:
        form = AddGlassSplitterPrestartForm(use_required_attribute=False)
    context = {
        'form': form,
    }
    return render(request, 'prestart/gilson_prestart.html', context)


def drop_weight_prestart(request):
    form = AddDropWeightPrestartForm(request.POST)

    # Filter the 'equip_name' field queryset based on your criteria
    # For example, let's say you want to show only certain equipment names
    filtered_equip_names = Equipment.objects.filter(equip_group__equip_group__iexact='DWT')
    print(filtered_equip_names)
    form.fields['equip_name'].queryset = filtered_equip_names
    if form.is_valid():
        form.save()
        return redirect('prestart_app:pre_thank')
    else:
        form = AddDropWeightPrestartForm(use_required_attribute=False)
    context = {
        'form': form,
    }
    return render(request, 'prestart/gilson_prestart.html', context)


def wet_mill_prestart(request):
    form = AddWetMillPrestartForm(request.POST)

    # Filter the 'equip_name' field queryset based on your criteria
    # For example, let's say you want to show only certain equipment names
    filtered_equip_names = Equipment.objects.filter(equip_group__equip_group__iexact='Wet-Mill')
    print(filtered_equip_names)
    form.fields['equip_name'].queryset = filtered_equip_names
    if form.is_valid():
        form.save()
        return redirect('prestart_app:pre_thank')
    else:
        form = AddWetMillPrestartForm(use_required_attribute=False)
    context = {
        'form': form,
    }
    return render(request, 'prestart/gilson_prestart.html', context)


def sonic_bath_prestart(request):
    form = AddSonicBathPrestartForm(request.POST)

    # Filter the 'equip_name' field queryset based on your criteria
    # For example, let's say you want to show only certain equipment names
    filtered_equip_names = Equipment.objects.filter(equip_group__equip_group__iexact='Sonic')
    print(filtered_equip_names)
    form.fields['equip_name'].queryset = filtered_equip_names
    if form.is_valid():
        form.save()
        return redirect('prestart_app:pre_thank')
    else:
        form = AddSonicBathPrestartForm(use_required_attribute=False)
    context = {
        'form': form,
    }
    return render(request, 'prestart/gilson_prestart.html', context)


def pulveriser_prestart(request):
    form = AddPulveriserPrestartForm(request.POST)

    # Filter the 'equip_name' field queryset based on your criteria
    # For example, let's say you want to show only certain equipment names
    filtered_equip_names = Equipment.objects.filter(equip_group__equip_group__iexact='Pulveriser')
    print(filtered_equip_names)
    form.fields['equip_name'].queryset = filtered_equip_names
    if form.is_valid():
        form.save()
        return redirect('prestart_app:pre_thank')
    else:
        form = AddPulveriserPrestartForm(use_required_attribute=False)
    context = {
        'form': form,
    }
    return render(request, 'prestart/pulveriser_prestart.html', context)


def large_crusher_prestart(request):
    form = AddLargeCrusherPrestartForm(request.POST)

    # Filter the 'equip_name' field queryset based on your criteria
    # For example, let's say you want to show only certain equipment names
    filtered_equip_names = Equipment.objects.filter(equip_group__equip_group__iexact='Crusher')
    print(filtered_equip_names)
    form.fields['equip_name'].queryset = filtered_equip_names
    if form.is_valid():
        form.save()
        return redirect('prestart_app:pre_thank')
    else:
        form = AddLargeCrusherPrestartForm(use_required_attribute=False)
    context = {
        'form': form,
    }
    return render(request, 'prestart/large_crusher_prestart.html', context)

def gold_conc_prestart(request):
    form = AddGoldConcPrestartForm(request.POST)

    # Filter the 'equip_name' field queryset based on your criteria
    # For example, let's say you want to show only certain equipment names
    filtered_equip_names = Equipment.objects.filter(equip_group__equip_group__iexact='Gold-Conc')
    print(filtered_equip_names)
    form.fields['equip_name'].queryset = filtered_equip_names
    if form.is_valid():
        form.save()
        return redirect('prestart_app:pre_thank')
    else:
        form = AddGoldConcPrestartForm(use_required_attribute=False)
    context = {
        'form': form,
    }
    return render(request, 'prestart/gold_conc_prestart.html', context)


def vacuum_filter_prestart(request):
    form = AddVacuumFilterPrestartForm(request.POST)

    # Filter the 'equip_name' field queryset based on your criteria
    # For example, let's say you want to show only certain equipment names
    filtered_equip_names = Equipment.objects.filter(equip_group__equip_group__iexact='Vacuum-Filter')
    print(filtered_equip_names)
    form.fields['equip_name'].queryset = filtered_equip_names
    if form.is_valid():
        form.save()
        return redirect('prestart_app:pre_thank')
    else:
        form = AddVacuumFilterPrestartForm(use_required_attribute=False)
    context = {
        'form': form,
    }
    return render(request, 'prestart/vacuum_filter_prestart.html', context)


def float_unit_prestart(request):
    form = AddFloatUnitPrestartForm(request.POST)

    # Filter the 'equip_name' field queryset based on your criteria
    # For example, let's say you want to show only certain equipment names
    filtered_equip_names = Equipment.objects.filter(equip_group__equip_group__iexact='Flotation-Unit')
    print(filtered_equip_names)
    form.fields['equip_name'].queryset = filtered_equip_names
    if form.is_valid():
        form.save()
        return redirect('prestart_app:pre_thank')
    else:
        form = AddFloatUnitPrestartForm(use_required_attribute=False)
    context = {
        'form': form,
    }
    return render(request, 'prestart/float_unit_prestart.html', context)


def fume_hood_prestart(request):
    form = AddFumeHoodPrestartForm(request.POST)

    # Filter the 'equip_name' field queryset based on your criteria
    # For example, let's say you want to show only certain equipment names
    filtered_equip_names = Equipment.objects.filter(equip_group__equip_group__iexact='Fume-Hood')
    print(filtered_equip_names)
    form.fields['equip_name'].queryset = filtered_equip_names
    if form.is_valid():
        form.save()
        return redirect('prestart_app:pre_thank')
    else:
        form = AddFumeHoodPrestartForm(use_required_attribute=False)
    context = {
        'form': form,
    }
    return render(request, 'prestart/fume_hood_prestart.html', context)


def mix_tank_prestart(request):
    form = AddMixTankPrestartForm(request.POST)

    # Filter the 'equip_name' field queryset based on your criteria
    # For example, let's say you want to show only certain equipment names
    filtered_equip_names = Equipment.objects.filter(equip_group__equip_group__iexact='Mixing-Tank')
    print(filtered_equip_names)
    form.fields['equip_name'].queryset = filtered_equip_names
    if form.is_valid():
        form.save()
        return redirect('prestart_app:pre_thank')
    else:
        form = AddMixTankPrestartForm(use_required_attribute=False)
    context = {
        'form': form,
    }
    return render(request, 'prestart/mix_tank_prestart.html', context)


def size_analyser_prestart(request):
    form = AddSizeAnalyserPrestartForm(request.POST)

    # Filter the 'equip_name' field queryset based on your criteria
    # For example, let's say you want to show only certain equipment names
    filtered_equip_names = Equipment.objects.filter(equip_group__equip_group__iexact='Sizer-Analyser')
    print(filtered_equip_names)
    form.fields['equip_name'].queryset = filtered_equip_names
    if form.is_valid():
        form.save()
        return redirect('prestart_app:pre_thank')
    else:
        form = AddSizeAnalyserPrestartForm(use_required_attribute=False)
    context = {
        'form': form,
    }
    return render(request, 'prestart/size_analyser_prestart.html', context)


def cyclone_rig_prestart(request):
    form = AddCycloneRigPrestartForm(request.POST)

    # Filter the 'equip_name' field queryset based on your criteria
    # For example, let's say you want to show only certain equipment names
    filtered_equip_names = Equipment.objects.filter(equip_group__equip_group__iexact='Cyclone-Rig')
    print(filtered_equip_names)
    form.fields['equip_name'].queryset = filtered_equip_names
    if form.is_valid():
        form.save()
        return redirect('prestart_app:pre_thank')
    else:
        form = AddCycloneRigPrestartForm(use_required_attribute=False)
    context = {
        'form': form,
    }
    return render(request, 'prestart/cyclone_rig_prestart.html', context)


def cyclo_sizer_prestart(request):
    form = AddCycloneSizerPrestartForm(request.POST)

    # Filter the 'equip_name' field queryset based on your criteria
    # For example, let's say you want to show only certain equipment names
    filtered_equip_names = Equipment.objects.filter(equip_group__equip_group__iexact='Cyclo-Sizer')
    print(filtered_equip_names)
    form.fields['equip_name'].queryset = filtered_equip_names
    if form.is_valid():
        form.save()
        return redirect('prestart_app:pre_thank')
    else:
        form = AddCycloneSizerPrestartForm(use_required_attribute=False)
    context = {
        'form': form,
    }
    return render(request, 'prestart/cyclo_sizer_prestart.html', context)

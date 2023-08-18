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



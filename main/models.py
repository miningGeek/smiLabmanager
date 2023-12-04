from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

# Create your models here.
shift = [
    ('All Day', 'All Day'),
    ('Morning', 'Morning'),
    ('Afternoon', 'Afternoon'),
]

status_choice = [
    ('Approved', 'Approved'),
    ('Completed', 'Completed'),
    ('Rejected', 'Rejected'),
    ('Cancelled', 'Cancelled'),
    ('Pending', 'Pending'),
]
basic_confirm = [
    ('Yes', 'Yes'),
    ('No', 'No'),
]
confirm = [
    ('Yes', 'Yes'),
    ('No', 'No'),
    ('NA', 'NA'),
]

sample_status = [
    ('Not Received','Not Received'),
    ('Received','Received'),
    ('Disposed','Disposed'),
    ('Returned','Returned'),
    ('Quarantine','Quarantine'),
]

class StatusChoice(models.Model):
    status = models.CharField(max_length=30)

    def __str__(self):
        return self.status


class ResearchCentres(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


# class Group(models.Model):
#     name = models.CharField(max_length=250)
#     centres = models.ForeignKey(ResearchCentres, on_delete=models.SET_NULL, null=True)
#     status_active = models.BooleanField(default=True)
#
#     def __str__(self):
#         return self.name


class ResearchGroup(models.Model):
    name = models.CharField(max_length=250)
    centres = models.ForeignKey(ResearchCentres, on_delete=models.SET_NULL, null=True)
    status_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    proj_number = models.CharField(max_length=10)
    ciloxis_num = models.CharField(max_length=100)
    group = models.ForeignKey(ResearchGroup, on_delete=models.SET_NULL, null=True)
    proj_concat = models.CharField(max_length=60, blank=True)

    def save(self, *args, **kwargs):
        self.proj_concat = f"{self.ciloxis_num}-{self.proj_number}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.proj_concat


class Client(models.Model):
    company_name = models.CharField(max_length=150)

    def __str__(self):
        return self.company_name


class ClientSite(models.Model):
    site_name = models.CharField(max_length=250)
    company_name = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.site_name


class ClientContact(models.Model):
    client_name = models.CharField(max_length=350)
    client_number = models.IntegerField()
    client_email = models.CharField(max_length=500)
    company_name = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    site_name = models.ForeignKey(ClientSite, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.client_name

class Building(models.Model):
    building_name = models.CharField(max_length=100)

    def __str__(self):
        return self.building_name


class BuildingLevel(models.Model):
    level_name = models.CharField(max_length=100)

    def __str__(self):
        return self.level_name


class Rooms(models.Model):
    room_number = models.CharField(max_length=10)
    room_name = models.CharField(max_length=50)
    building_level = models.ForeignKey('BuildingLevel', on_delete=models.SET_NULL, null=True)
    building = models.ForeignKey('Building', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.room_name


class EquipmentGroup(models.Model):
    equip_group = models.CharField(max_length=250)

    def __str__(self):
        return self.equip_group


class Equipment(models.Model):
    equip_name = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    room = models.ForeignKey(Rooms, on_delete=models.SET_NULL, null=True)
    building_level = models.ForeignKey('BuildingLevel', on_delete=models.SET_NULL, null=True)
    building = models.ForeignKey('Building', on_delete=models.SET_NULL, null=True)
    is_equip = models.BooleanField(blank=True, null=True)
    equip_group = models.ForeignKey(EquipmentGroup, on_delete=models.SET_NULL,null=True, blank=True)
    group_owner = models.ForeignKey(ResearchGroup, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.equip_name


class AppUser(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=25, blank=True)
    centre = models.ForeignKey('ResearchCentres', on_delete=models.SET_NULL, null=True)
    group = models.ForeignKey('ResearchGroup', on_delete=models.SET_NULL, null=True)
    status_active = models.BooleanField(default=True)
    ute_auth = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ['user_name__username']


class Booking(models.Model):
    user_name = models.ForeignKey(AppUser, on_delete=models.SET_NULL, null=True, blank=True)
    proj_data = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True)
    request_date = models.DateTimeField(default=timezone.now)
    group = models.ForeignKey(ResearchGroup, on_delete=models.SET_NULL, null=True, blank=True)
    equip_name = models.ForeignKey(Equipment, on_delete=models.SET_NULL, null=True)
    start_date = models.DateField()
    shift = models.CharField(max_length=50, choices=shift, blank=True, default='All Day')
    num_hours = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=50, choices=status_choice, blank=True, default='Pending')

    def user_first_name(self):
        return self.user_name.first_name

    def get_html_url(self):
        url = reverse('main_app:edit_booking', args=[self.pk])
        return f'<a href="{url}">{self.user_name}</a>'


class Location(models.Model):

    location = models.CharField(max_length=50)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.location


class PrestartCheck(models.Model):
    username = models.ForeignKey(AppUser, on_delete=models.SET_NULL, null=True, blank=True)
    equip_name = models.ForeignKey(Equipment, on_delete=models.SET_NULL, null=True)
    prestart_date = models.DateTimeField(default=timezone.now)
    trained = models.CharField(max_length=10, choices=basic_confirm)
    sop_ra = models.CharField(max_length=10, choices=basic_confirm)
    test_tag = models.CharField(max_length=10, choices=basic_confirm, blank=True)
    elect_lead = models.CharField(max_length=10, choices=basic_confirm, blank=True)
    stop_button = models.CharField(max_length=10, choices=confirm, blank=True)
    safety_stop = models.CharField(max_length=10, choices=confirm, blank=True)
    guarding = models.CharField(max_length=10, choices=confirm, blank=True)
    interlock = models.CharField(max_length=10, choices=confirm, blank=True)
    rubber_strap = models.CharField(max_length=10, choices=confirm, blank=True)
    dust_extract = models.CharField(max_length=10, choices=confirm, blank=True)
    counter = models.CharField(max_length=10, choices=confirm, blank=True)
    hyd_pump = models.CharField(max_length=10, choices=confirm, blank=True)
    hyd_oil_level = models.CharField(max_length=10, choices=confirm, blank=True)
    water_elect =models.CharField(max_length=10, choices=confirm, blank=True)
    water_level = models.CharField(max_length=10, choices=confirm, blank=True)
    air_pressure = models.CharField(max_length=10, choices=confirm, blank=True)
    cable = models.CharField(max_length=10, choices=confirm, blank=True)
    seals = models.CharField(max_length=10, choices=confirm, blank=True)
    drainage = models.CharField(max_length=10, choices=confirm, blank=True)
    housekeeping = models.CharField(max_length=10, choices=confirm, blank=True)
    anti_slip = models.CharField(max_length=10, choices=confirm, blank=True)
    noise_baffles = models.CharField(max_length=10, choices=confirm, blank=True)
    filter_mat = models.CharField(max_length=10, choices=confirm, blank=True)
    glass_bott = models.CharField(max_length=10, choices=confirm, blank=True)
    fume_filter = models.CharField(max_length=10, choices=confirm, blank=True)
    battery_water = models.CharField(max_length=10, choices=confirm, blank=True)
    battery_condition = models.CharField(max_length=10, choices=confirm, blank=True)
    mill_param = models.CharField(max_length=10, choices=confirm, blank=True)
    comments = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.equip_name


class Sample(models.Model):
    tracking_id = models.IntegerField(blank=True)
    sample_owner = models.ForeignKey(AppUser, on_delete=models.SET_NULL, null=True, blank=True)
    centre_owner = models.ForeignKey(ResearchCentres, on_delete=models.SET_NULL, null=True, blank=True)
    group_owner = models.ForeignKey(ResearchGroup, on_delete=models.SET_NULL, null=True, blank=True)
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True)
    client_site = models.ForeignKey(ClientSite, on_delete=models.SET_NULL, null=True)
    client_contact = models.ForeignKey(ClientContact, on_delete=models.SET_NULL, null=True)
    sample_location = models.ManyToManyField(Location, blank=True)
    description = models.TextField(max_length=500, blank=True)
    sample_status = models.CharField(max_length=25, choices=sample_status, blank=True)
    hazard_advice = models.BooleanField(blank=True, null=True)
    date_received = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.tracking_id













from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
shift = [
    ('All Day', 'All Day'),
    ('Morning', 'Morning'),
    ('Afternoon', 'Afternoon'),
]

status_choice = [
    ('Approved', 'Approved'),
    ('Rejected', 'Rejected'),
    ('Canceled', 'Canceled'),
    ('Pending', 'Pending'),
]


class StatusChoice(models.Model):
    status = models.CharField(max_length=30)

    def __str__(self):
        return self.status


class ResearchCentres(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=250)
    centres = models.ForeignKey(ResearchCentres, on_delete=models.SET_NULL, null=True)
    status_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Client(models.Model):
    company_name = models.CharField(max_length=150)
    site_name = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    site_contact_name = models.CharField(max_length=250, blank=True)
    site_contact_email = models.CharField(max_length=250, blank=True)
    client_concat_name = models.CharField(max_length=300)

    def save(self, *args, **kwargs):
        self.client_concat_name = f"{self.company_name} {self.site_name}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.client_concat_name


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


class Equipment(models.Model):
    equip_name = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    room = models.ForeignKey(Rooms, on_delete=models.SET_NULL, null=True)
    building_level = models.ForeignKey('BuildingLevel', on_delete=models.SET_NULL, null=True)
    building = models.ForeignKey('Building', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.equip_name


class AppUser(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    centre = models.ForeignKey('ResearchCentres', on_delete=models.SET_NULL, null=True)
    group = models.ForeignKey('Group', on_delete=models.SET_NULL, null=True)


class Booking(models.Model):
    user_name = models.ForeignKey(AppUser, on_delete=models.SET_NULL, null=True, blank=True)
    request_date = models.DateField(auto_now_add=True)
    equip_name = models.ForeignKey(Equipment, on_delete=models.SET_NULL, null=True)
    start_date = models.DateField()
    shift = models.CharField(max_length=50, choices=shift, blank=True, default='All Day')
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









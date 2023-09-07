from django.urls import path
from . import views

app_name = 'sample_app'

urlpatterns = [
    path('sample_home', views.sample_home, name='sample_home'),
    path('add_sample', views.add_sample, name='add_sample'),
    path('delete_sample/<sample_id>', views.delete_sample, name='delete_sample'),
    path('sample_location', views.sample_location, name='sample_location'),
    path('edit_sample_location/<location_id>', views.edit_sample_location, name='edit_sample_location'),
    path('delete_sample_location/<location_id>', views.delete_sample_location, name='delete_sample_location'),
    path('sample_client', views.sample_client, name='sample_client'),
    path('edit_sample_client/<client_id>', views.edit_sample_client, name='edit_sample_client'),
    path('delete_sample_client/<client_id>', views.delete_sample_client, name='delete_sample_client'),
    path('sample_client_site', views.sample_client_site, name='sample_client_site'),

]
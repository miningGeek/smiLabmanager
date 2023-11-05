from django.urls import path
from . import views

app_name = 'report_app'

urlpatterns = [
    path('report_home', views.report_home, name='report_home'),
    path('report_jkmrc', views.report_jkmrc, name='report_jkmrc'),
    path('report_jktech', views.report_jktech, name='report_jktech'),
    path('bookings_csv', views.bookings_csv, name='bookings_csv'),
    path('equipment_csv', views.equipment_csv, name='equipment_csv'),
    path('prestart_csv', views.prestart_csv, name='prestart_csv'),
]
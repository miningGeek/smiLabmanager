from django.urls import path
from . import views

app_name = 'report_app'

urlpatterns = [
    path('report_home', views.report_home, name='report_home'),
]
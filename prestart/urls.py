from django.urls import path
from . import views

app_name = 'prestart_app'

urlpatterns = [
    path('pre_home', views.pre_home, name='pre_home'),
    path('pre_thank', views.pre_thank, name='pre_thank'),
    path('prestart_list', views.prestart_list, name='prestart_list'),
    path('rotap_prestart', views.rotap_prestart, name='rotap_prestart'),
    path('large_splitter_prestart', views.large_splitter_prestart, name='large_splitter_prestart'),
    path('small_jaw_prestart', views.small_jaw_prestart, name='small_jaw_prestart'),
    path('filter_press_prestart', views.filter_press_prestart, name='filter_press_prestart'),

]
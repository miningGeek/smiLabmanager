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
    path('gilson_prestart', views.gilson_prestart, name='gilson_prestart'),
    path('wet_sieve_prestart', views.wet_sieve_prestart, name='wet_sieve_prestart'),
    path('ball_mill_prestart', views.ball_mill_prestart, name='ball_mill_prestart'),
    path('glass_splitter_prestart', views.glass_splitter_prestart, name='glass_splitter_prestart'),
    path('drop_weight_prestart', views.drop_weight_prestart, name='drop_weight_prestart'),
    path('wet_mill_prestart', views.wet_mill_prestart, name='wet_mill_prestart'),
    path('sonic_bath_prestart', views.sonic_bath_prestart, name='sonic_bath_prestart'),
    path('pulveriser_prestart', views.pulveriser_prestart, name='pulveriser_prestart'),
    path('large_crusher_prestart', views.large_crusher_prestart, name='large_crusher_prestart'),
    path('gold_conc_prestart', views.gold_conc_prestart, name='gold_conc_prestart'),
    path('vacuum_filter_prestart', views.vacuum_filter_prestart, name='vacuum_filter_prestart'),
    path('float_unit_prestart', views.float_unit_prestart, name='float_unit_prestart'),
    path('fume_hood_prestart', views.fume_hood_prestart, name='fume_hood_prestart'),
    path('mix_tank_prestart', views.mix_tank_prestart, name='mix_tank_prestart'),
    path('size_analyser_prestart', views.size_analyser_prestart, name='size_analyser_prestart'),
    path('cyclone_rig_prestart', views.cyclone_rig_prestart, name='cyclone_rig_prestart'),
    path('cyclo_sizer_prestart', views.cyclo_sizer_prestart, name='cyclo_sizer_prestart'),

]
from django.urls import path
from . import views

app_name = 'main_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('building_list', views.building_list, name="building_list"),
    path('edit_building_list/<building_id>', views.edit_building_list, name="edit_building_list"),
    path('delete_building_list/<building_id>', views.delete_building_list, name="delete_building_list"),
    path('build_level', views.build_level, name="build_level"),
    path('edit_build_level/<level_id>', views.edit_build_level, name="edit_build_level"),
    path('delete_build_level/<level_id>', views.delete_build_level, name="delete_build_level"),
    path('build_room', views.build_room, name="build_room"),
    path('edit_build_room/<room_id>', views.edit_build_room, name="edit_build_room"),
    path('delete_build_room/<room_id>', views.delete_build_room, name="delete_build_room"),
    path('equip_list', views.equip_list, name="equip_list"),
    path('edit_equip_list/<equip_id>', views.edit_equip_list, name="edit_equip_list"),
    path('delete_equip_list/<equip_id>', views.delete_equip_list, name="delete_equip_list"),
    path('research_cent', views.research_cent, name="research_cent"),
    path('edit_research_cent/<centre_id>', views.edit_research_cent, name="edit_research_cent"),
    path('delete_research_cent/<centre_id>', views.delete_research_cent, name="delete_research_cent"),
    path('group', views.group, name='group'),
    path('edit_group/<group_id>', views.edit_group, name='edit_group'),
    path('delete_group/<group_id>', views.delete_group, name='delete_group'),
    path('booking/', views.booking, name='booking'),
    path('edit_booking/<booking_id>', views.edit_booking, name='edit_booking'),
    path('delete_booking/<booking_id>', views.delete_booking, name='delete_booking'),
    path('booking_calendar/<str:room_name>', views.booking_calendar.as_view(), name='booking_calendar'),
    path('status_choice', views.status_choice, name="status_choice"),
    path('edit_status_choice/<status_id>', views.edit_status_choice, name="edit_status_choice"),
    path('delete_status_choice/<status_id>', views.delete_status_choice, name="delete_status_choice"),
    path('get_rooms',views.get_rooms, name='get_rooms'),
    path('get_equipments',views.get_equipments,name='get_equipments'),
    path('get_projects',views.get_projects, name='get_projects'),
    path('add_user', views.add_user, name='add_user'),
    path('edit_add_user/<user_id>', views.edit_add_user, name='edit_add_user'),
    path('delete_add_user/<user_id>', views.delete_add_user, name='delete_add_user'),
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('add_project', views.add_project, name='add_project'),
    path('edit_add_project/<project_id>', views.edit_add_project, name='edit_add_project'),
    path('delete_add_project/<project_id>', views.delete_add_project, name='delete_add_project'),
    path('equip_group', views.add_equip_group, name='add_equip_group'),
    path('monthly_report_form', views.monthly_report_form, name ='monthly_report_form'),
    path('generate_monthly_report', views.generate_monthly_report, name='generate_monthly_report'),


]

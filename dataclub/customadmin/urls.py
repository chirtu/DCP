from . import views
from django.urls import path

urlpatterns = [

    path('', views.admin_login, name='login'),
    path('dashboard/', views.admin_home, name='home'),
    
    path('dashboard/', views.admin_home, name='home'),
    path('abouts/', views.admin_abouts, name='abouts'),
    path('members/', views.admin_members, name='members'),
    path('events/', views.admin_events, name='events'),
    path('resources/', views.admin_resources, name='resources'),
    path('add_abouts/', views.admin_add_about, name='add_abouts'),
]

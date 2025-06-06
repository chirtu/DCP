from . import views
from django.urls import path

urlpatterns = [

    path('',views.home, name='home'),
    # path('events/', views.events, name='events'),
    # path('resources/', views.resources, name='resources'),
    # path('members/', views.members, name='members'),
    # path('contacts/', views.contact, name='contacts'),
    
    
]

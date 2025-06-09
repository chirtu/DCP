from . import views
from django.urls import path

urlpatterns = [

    # path('',views.customadmin, name='home'),
    path('', views.admin_home, name='register'),

    
]

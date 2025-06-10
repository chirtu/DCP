from . import views
from django.urls import path

urlpatterns = [

    path('', views.admin_login, name='login'),
    path('dashboard/', views.admin_home, name='home'),
   
]

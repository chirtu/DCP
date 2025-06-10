from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def registerPage(request):
    form = UserCreationForm()
    context = {}
    return render(request, 'customadmin/register.html',context)
 
def admin_login(request):
    return render(request, 'customadmin/login.html')

def admin_home(request):
    return render(request, 'customadmin/home.html')

def admin_events(request):
    return render(request, 'customadmin/pages/events.html')

def admin_abouts(request):
    return render(request, 'customadmin/pages/about.html')

def admin_resources(request):
    return render(request, 'customadmin/pages/resources.html')

def admin_members(request):
    return render(request, 'customadmin/pages/members.html')
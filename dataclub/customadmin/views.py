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


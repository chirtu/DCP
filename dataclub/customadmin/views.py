from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def registerPage(request):
    form = UserCreationForm()
    context = {}
    return render(request, 'core/register.html',context)
 
def admin_home(request):
    return render(request, 'core/login.html')
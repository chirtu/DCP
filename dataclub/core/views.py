from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

def events(request):
    return render(request, 'core/events.html')

def resources(request):
    return render(request, 'core/resources.html')

def members(request):
    return render(request, 'core/members.html')

def contact(request):
    return render(request, 'core/contact.html')

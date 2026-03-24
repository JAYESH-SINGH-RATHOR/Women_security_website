from urllib import request

from django.shortcuts import render , HttpResponse
from .models import *
# Create your views here.

def home(request):
    return render(request , "home.html")

def about(request):
    return render(request , "about.html")

def contact(request):
    if request.method == "POST":
        name =  request.POST.get("name")
        emercont =  request.POST.get("emercont")
        phone = request.POST.get("phone")
        location = request.POST.get("location")
        msg = request.POST.get("msg")
        currlocation = request.POST.get("currlocation")
        coords = request.POST.get("coords")
        media = request.POST.get("media")
        urgent = EmergencyUser(
            name = name , emercont = emercont ,
            phone = phone , location = location , msg = msg,
            currlocation = currlocation , coords = coords ,
            media = media
        )
        urgent.save()
    return render(request , "contact.html")

def login(request):
    return render(request , "login.html")

def register(request):
    return render(request , "registration.html")
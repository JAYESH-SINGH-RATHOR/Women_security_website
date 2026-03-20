from urllib import request

from django.shortcuts import render , HttpResponse
from .models import *
# Create your views here.

def home(request):
    return render(request , "home.html")

def about(request):
    return render(request , "about.html")

def contact(request):
    return render(request , "contact.html")

def login(request):
    return render(request , "login.html")

def register(request):
    return render(request , "registration.html")
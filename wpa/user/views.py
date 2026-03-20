from django.shortcuts import render , HttpResponse
from .models import *
# Create your views here.

def home(request):
    return render(request , "navbar.html")
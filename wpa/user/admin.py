from django.contrib import admin
from .models import *
# Register your models here.

class EmergencyUserAdmin(admin.ModelAdmin):
    list_display =['id' , 'name' , 'emercont' ,'location' , 'phone' , 'msg' ,'currlocation','coords' ,'media']
admin.site.register(EmergencyUser , EmergencyUserAdmin)
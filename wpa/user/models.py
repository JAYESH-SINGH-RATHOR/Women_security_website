from django.db import models

# Create your models here.

class EmergencyUser(models.Model):
    name = models.CharField(max_length=100)
    emercont = models.CharField(max_length=10)
    phone = models.CharField(max_length=10)
    location = models.CharField(max_length=100)
    msg = models.CharField(max_length=1000)
    currlocation = models.CharField(max_length=100 , null=True, blank=True)
    coords = models.CharField(max_length=100 , null=True, blank=True)
    media = models.FileField(upload_to='')

    def __str__(self):
        return self.name
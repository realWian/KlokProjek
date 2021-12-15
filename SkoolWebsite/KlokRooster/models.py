from django.db import models
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
# from django.contrib.auth.models import User
import datetime
import time
from playsound import playsound
from pathlib import Path
import os

# Create your models here.
class Rooster(models.Model):
    naam = models.CharField(max_length=256, default="Nuwe Rooster")
    
    periode1 = models.TimeField(default="7:30")
    periode2 = models.TimeField(default="8:00")
    periode3 = models.TimeField(default="8:30")
    periode4 = models.TimeField(default="9:00")
    pouse1 = models.TimeField(default="9:30")
    periode5 = models.TimeField(default="9:45")
    periode6 = models.TimeField(default="10:15")
    periode7 = models.TimeField(default="10:45")
    periode8 = models.TimeField(default="11:15")
    pouse2 = models.TimeField(default="11:45")
    periode9 = models.TimeField(default="12:00")
    periode10 = models.TimeField(default="12:30")
    periode11 = models.TimeField(default="13:00")
    periode12 = models.TimeField(default="13:30")
    uitkomtyd = models.TimeField(default="14:00")

    luisterend = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse_lazy("KlokRooster:rooster", kwargs={"pk" : self.pk}) 

    def lui_klok(self):
        playsound(os.path.join(Path(__file__).resolve().parent, "static/audio/Skoolklok_audio.m4a"))

    def luister_vir_lui(self, luiTye):
        while get_object_or_404(Rooster, pk=self.pk).luisterend:
            if datetime.datetime.now().strftime("%H:%M:%S") == luiTye[-1]:
                self.lui_klok()
                break
            if datetime.datetime.now().strftime("%H:%M:%S") in luiTye:
                self.lui_klok()

    def __str__(self):
        return self.naam

# class UserProfileInfo(models.Model):
#     user = models.OneToOneField(User)
#     grade = models.PositiveIntegerField(max=12)

#     def __str__(self):
#         return self.user.username
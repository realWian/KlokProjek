"""SkoolWebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import KlokRooster.urls
from KlokRooster.models import Rooster
from django.shortcuts import get_object_or_404

urlpatterns = [
    path('', include(KlokRooster.urls)),
    path('admin/', admin.site.urls),
]

# Insures all roosters are deaf on startup.
rooster_list = Rooster.objects.all()
for rooster in rooster_list:
    rooster.luisterend = False
    rooster.save()
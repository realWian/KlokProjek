from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, DeleteView, UpdateView, ListView, DetailView
from KlokRooster.models import Rooster

# Create your views here.
class Index(TemplateView):
    template_name = 'index.html'

class RoosterListView(ListView):
    context_object_name = "roosters"
    model = Rooster
    template_name = "roosterlys.html"

class RoosterDetailView(DetailView):
    context_object_name = "rooster"
    model = Rooster
    template_name = "wys_rooster.html"

class RoosterUpdateView(UpdateView):
    model = Rooster
    fields = "__all__"
    template_name = "verander_rooster.html"

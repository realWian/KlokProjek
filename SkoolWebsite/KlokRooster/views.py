from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, DeleteView, UpdateView, ListView, DetailView
from KlokRooster.models import Rooster
from django.urls import reverse_lazy

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
    context_object_name = "rooster"
    model = Rooster
    fields = "__all__"
    template_name = "verander_rooster.html"

class RoosterCreateView(CreateView):
    model = Rooster
    fields ="__all__"
    template_name = "skep_rooster.html"

class RoosterDeleteView(DeleteView):
    context_object_name = "rooster"
    model = Rooster
    template_name = "skrap_rooster.html"
    success_url = reverse_lazy("KlokRooster:roosterlys")
    
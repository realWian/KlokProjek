from django.shortcuts import render, redirect, get_object_or_404
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

def luister_vir_lui(request, pk):
    model = get_object_or_404(Rooster, pk=pk)
    model.luisterend = True
    model.save()
    luiTye = [
        model.periode1.strftime("%H:%M:%S"), 
        model.periode2.strftime("%H:%M:%S"),
        model.periode3.strftime("%H:%M:%S"), 
        model.periode4.strftime("%H:%M:%S"),
        model.pouse1.strftime("%H:%M:%S"),
        model.periode5.strftime("%H:%M:%S"), 
        model.periode6.strftime("%H:%M:%S"), 
        model.periode7.strftime("%H:%M:%S"), 
        model.periode8.strftime("%H:%M:%S"),
        model.pouse2.strftime("%H:%M:%S"), 
        model.periode9.strftime("%H:%M:%S"),
        model.periode10.strftime("%H:%M:%S"), 
        model.periode11.strftime("%H:%M:%S"), 
        model.periode12.strftime("%H:%M:%S"), 
        model.uitkomtyd.strftime("%H:%M:%S")
    ]
    model.luister_vir_lui(luiTye)
    return redirect(model.get_absolute_url())

def verdoof(request, pk):
    model = get_object_or_404(Rooster, pk=pk)
    model.luisterend = False
    model.save()
    return redirect(model.get_absolute_url())

def lui_klok(request, pk):
    model = get_object_or_404(Rooster, pk=pk)
    model.lui_klok()
    return redirect(model.get_absolute_url())

class RoosterDetailView(DetailView):
    context_object_name = "rooster"
    model = Rooster
    template_name = "wys_rooster.html"

class RoosterUpdateView(UpdateView):
    context_object_name = "rooster"
    model = Rooster
    fields = ("naam", "periode1", "periode2", "periode3", "periode4", "pouse1", "periode5", "periode6", "periode7", "periode8", "pouse2", "periode9", "periode10", "periode11", "periode12", "uitkomtyd")
    template_name = "verander_rooster.html"

class RoosterCreateView(CreateView):
    model = Rooster
    fields = ("naam", "periode1", "periode2", "periode3", "periode4", "pouse1", "periode5", "periode6", "periode7", "periode8", "pouse2", "periode9", "periode10", "periode11", "periode12", "uitkomtyd")
    template_name = "skep_rooster.html"

class RoosterDeleteView(DeleteView):
    context_object_name = "rooster"
    model = Rooster
    template_name = "skrap_rooster.html"
    success_url = reverse_lazy("KlokRooster:roosterlys")
    
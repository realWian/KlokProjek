from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, CreateView, DeleteView, UpdateView, ListView, DetailView
from KlokRooster.models import Rooster
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
import datetime

# Create your views here.
class Index(TemplateView):
    template_name = 'index.html'

class RoosterAuthenticationForm(AuthenticationForm):
    error_messages = {
        'invalid_login' : ("Die gegewe besonderhede was ongeldig. Probeer weer of kontak die administrateur."),
        'inactive' : ("Hierdie rekening is tans onaktief.")
    }

    def __init__(self, *args, **kwargs):
        super(RoosterAuthenticationForm, self).__init__(*args, **kwargs)
        self.fields["username"].label = "Noemnaam:"
        self.fields["password"].label = "Wagwoord:"
    
class RoosterLoginView(LoginView):
    template_name = "login.html"
    authentication_form = RoosterAuthenticationForm

class RoosterListView(LoginRequiredMixin, ListView):
    context_object_name = "roosters"
    model = Rooster
    template_name = "roosterlys.html"

@login_required
def luister_vir_lui(request, pk):
    model = get_object_or_404(Rooster, pk=pk)
    model.luisterend = True
    model.save()
    luiTye = [
        model.AantreeTyd.strftime("%H:%M:%S"),
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
    print("Luisterend: " + datetime.datetime.now().strftime("%H:%M:%S"))
    model.luister_vir_lui(luiTye)
    model.luisterend = False
    model.save()
    print("Doof: " + datetime.datetime.now().strftime("%H:%M:%S"))
    return redirect(model.get_absolute_url())

@login_required
def verdoof(request, pk):
    model = get_object_or_404(Rooster, pk=pk)
    model.luisterend = False
    model.save()
    print("Doof: " + datetime.datetime.now().strftime("%H:%M:%S"))
    return redirect(model.get_absolute_url())

@login_required
def lui_klok(request, pk):
    model = get_object_or_404(Rooster, pk=pk)
    model.lui_klok()
    return redirect(model.get_absolute_url())

class RoosterDetailView(LoginRequiredMixin, DetailView):
    context_object_name = "rooster"
    model = Rooster
    template_name = "wys_rooster.html"

class RoosterUpdateView(LoginRequiredMixin, UpdateView):
    context_object_name = "rooster"
    model = Rooster
    fields = ("naam", "aantreetyd", "periode1", "periode2", "periode3", "periode4", "pouse1", "periode5", "periode6", "periode7", "periode8", "pouse2", "periode9", "periode10", "periode11", "periode12", "uitkomtyd")
    template_name = "verander_rooster.html"

class RoosterCreateView(LoginRequiredMixin, CreateView):
    model = Rooster
    fields = ("naam", "aantreetyd", "periode1", "periode2", "periode3", "periode4", "pouse1", "periode5", "periode6", "periode7", "periode8", "pouse2", "periode9", "periode10", "periode11", "periode12", "uitkomtyd")
    template_name = "skep_rooster.html"

class RoosterDeleteView(LoginRequiredMixin, DeleteView):
    context_object_name = "rooster"
    model = Rooster
    template_name = "skrap_rooster.html"
    success_url = reverse_lazy("KlokRooster:roosterlys")
    
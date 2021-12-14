from django.urls import path
from KlokRooster.views import Index, RoosterListView, RoosterDetailView, RoosterUpdateView, RoosterCreateView, RoosterDeleteView, luister_vir_lui, verdoof, lui_klok

app_name = "KlokRooster"

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('roosterlys/', RoosterListView.as_view(), name="roosterlys"),
    path('rooster/<int:pk>/luisterend', luister_vir_lui, name="luister_vir_lui"),
    path('rooster/<int:pk>/verdoof', verdoof, name="verdoof"),
    path('rooster/<int:pk>/lui_klok', lui_klok, name="lui_klok"),
    path('rooster/<int:pk>/', RoosterDetailView.as_view(), name="rooster"),
    path('rooster/<int:pk>/verander', RoosterUpdateView.as_view(), name="verander_rooster"),
    path('skep_rooster', RoosterCreateView.as_view(), name="skep_rooster"),
    path('rooster/<int:pk>/skrap', RoosterDeleteView.as_view(), name="skrap_rooster"),
]
from django.urls import path
from KlokRooster.views import RoosterListView, RoosterDetailView, RoosterUpdateView, RoosterCreateView, RoosterDeleteView

app_name = "KlokRooster"

urlpatterns = [
    path('roosterlys/', RoosterListView.as_view(), name="roosterlys"),
    path('rooster/<int:pk>/', RoosterDetailView.as_view(), name="rooster"),
    path('rooster/<int:pk>/verander', RoosterUpdateView.as_view(), name="verander_rooster"),
    path('skep_rooster', RoosterCreateView.as_view(), name="skep_rooster"),
    path('rooster/<int:pk>/skrap/', RoosterDeleteView.as_view(), name="skrap_rooster")
]
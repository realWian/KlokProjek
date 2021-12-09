from django.urls import path
from KlokRooster.views import RoosterListView, RoosterDetailView

app_name = "KlokRooster"

urlpatterns = [
    path('roosterlys/', RoosterListView.as_view(), name="roosterlys"),
    path('rooster/<int:pk>/', RoosterDetailView.as_view(), name="rooster"),
]
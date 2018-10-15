from django.urls import path
from .views import ListPlayerView
from .views import PlayerDetailedView

urlpatterns = [
    path('player/', ListPlayerView.as_view(), name="players-all"),
    path('player/<int:dota2_id>', PlayerDetailedView.as_view(), name="players-details")
]
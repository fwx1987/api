from django.contrib import admin
from django.urls import path,include

from django.urls import path
from .views import ListSongsView


urlpatterns = [
    path('songs/', ListSongsView.as_view(), name="songs-all")
]
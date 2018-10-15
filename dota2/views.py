from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from .models import Player
from .serializers import PlayerSerializer

import logging

class ListPlayerView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class PlayerDetailedView(generics.ListAPIView):

    def getPlayerDetails(self):
        request = self.request.dota2_id
        print(self.request)
        return Player.objects.filter(dota2_id=request)


    serializer_class =  PlayerSerializer


    def get_queryset(self):
        #result = Player.objects.get(self.request.dota2_id)
        
        logging.info(self.request.data)
        return


from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets,filters
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

class MusicsView(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer

class SearchingViewMusic(generics.ListCreateAPIView):
    search_fields = ['name','artist__psevdo_name']
    filter_backends = (filters.SearchFilter,)
    queryset = Music.objects.all()
    serializer_class = MusicSerializer

class FavoriteView(APIView):
    def get(self,request,format=None):
        fav = FavoriteMusic.objects.all()
        serializer = FavoriteSerializer(fav,many=True)
        return Response(serializer.data)

class PlaylistView(APIView):
    def get(self,request,format=None):
        queryset = Playlist_Track.objects.all()
        serializer = PlaylistTrackSerializer(queryset,many=True)
        return Response(serializer.data)

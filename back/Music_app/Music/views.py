from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response


class MusicsView(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer


class FavoriteView(APIView):
    def get(self,request,format=None):
        fav = FavoriteMusic.objects.all()
        serializer = FavoriteSerializer(fav,many=True)
        return Response(serializer.data)
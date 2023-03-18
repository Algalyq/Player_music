from django.shortcuts import render


from .serializers import *
from rest_framework import viewsets
from .models import *

class MusicsView(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer

from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import *
from rest_framework import generics

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


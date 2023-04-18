from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import *
from rest_framework import generics

from rest_framework.generics import UpdateAPIView
# from rest_framework.permissions import IsAuthenticated
from .serializers import CustomUserSerializer

class CustomUserImageUpdate(UpdateAPIView):
    serializer_class = CustomUserSerializer
    # permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer


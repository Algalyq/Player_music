from .serializers import *
from rest_framework.views import APIView
from .models import *
from rest_framework.response import Response
from .serializers import *
from django.http import Http404
from rest_framework import status

class ArtistView(APIView):

    def get(self,request):
        query = Artist.objects.all()
        serializer = ArtistSerializer(query,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = ArtistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AlbumsView(APIView):

    def get(self,request):
        ...

    def post(self,request):
        ...


class TracksView(APIView):

    def get(self,request):
        ...
    
    def post(self,request):
        ...
        
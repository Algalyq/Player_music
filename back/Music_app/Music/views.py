from .serializers import *
from rest_framework.generics import APIView 

class ArtistView(APIView):

    def get(self,request):
        ...

    def post(self,request):
        ...


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
        
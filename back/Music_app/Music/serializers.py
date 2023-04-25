from rest_framework import serializers
from .models import *

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('artist_id','name','image')



class AlbumsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Albums
        fields = ('album_id','artist_id','name','release_date','image')
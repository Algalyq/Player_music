from rest_framework import serializers
from .models import *

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('artist_id','name','image')
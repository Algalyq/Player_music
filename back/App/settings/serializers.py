from rest_framework import serializers
from .models import *


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['psevdo_name']
class MusicSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer()
    class Meta:
        model = Music
        fields = ['name','cover','artist','audio','active']
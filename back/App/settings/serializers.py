from rest_framework import serializers
from .models import *


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['psevdo_name']

# class ColorsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Color
#         fields = ['music','color']

class MusicSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer()
    # music_color = ColorsSerializer()
    class Meta:
        model = Music
        fields = ["name","cover","artist","audio","id","active"]

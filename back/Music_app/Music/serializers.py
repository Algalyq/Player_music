from rest_framework import serializers
from .models import *

from django.contrib.auth.models import User

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


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

class FavoriteSerializer(serializers.ModelSerializer):
    music = MusicSerializer()
    user = UserSerializer()

    class Meta:
        model = FavoriteMusic
        fields = ['user','music']


class PlaylistSerializer(serializers.ModelSerializer):
    # music = MusicSerializer()
    # pltrack = PlaylistTrackSerializer()
    class Meta:
        model = Playlist
        fields = ['user_id','playlist_id','name']
        # exclude = []

class PlaylistTrackSerializer(serializers.ModelSerializer):
    music_id = MusicSerializer()
    playlist_id = PlaylistSerializer()
    class Meta: 
        model = Playlist_Track
        fields = ['playlist_id','music_id']

class Playlist_TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist_Track
        fields = ('__all__')


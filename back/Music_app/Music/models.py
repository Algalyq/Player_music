from django.db import models
from django.contrib.auth.models import User

class Artist(models.Model):
    psevdo_name = models.CharField(max_length=255)

class Music(models.Model):
    name = models.CharField(max_length=255)
    cover = models.ImageField(upload_to="images")
    audio = models.FileField(upload_to="music")
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    active = models.BooleanField(default=False)

class FavoriteMusic(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,db_index=True)
    music = models.ForeignKey('Music', on_delete=models.CASCADE)

class Playlist(models.Model):
    playlist_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False)

class Playlist_Track(models.Model):
    playlist_id = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    music_id = models.ForeignKey(Music, on_delete=models.CASCADE)


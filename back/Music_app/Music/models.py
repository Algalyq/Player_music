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

class Color(models.Model):
    music = models.ForeignKey('Music', on_delete=models.CASCADE)
    color = models.CharField(max_length=255)
from django.db import models


class Artist(models.Model):
    psevdo_name = models.CharField(max_length=255)

class Music(models.Model):
    name = models.CharField(max_length=255)
    cover = models.ImageField(upload_to="images")
    audio = models.FileField(upload_to="music")
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    active = models.BooleanField(default=False)
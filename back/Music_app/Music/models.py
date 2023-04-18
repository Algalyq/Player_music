from django.db import models
from django.contrib.auth.models import User
from Auth.models import CustomUser
from composite_field import CompositeField


class Artist(models.Model):
    artist_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,null=True)
    genre = models.CharField(max_length=50)
    image = models.ImageField(upload_to='artist_images', null=True, blank=True)


class Albums(models.Model):
    album_id = models.AutoField(primary_key=True)
    artist_id = models.ForeignKey('Artist', on_delete=models.CASCADE)
    name = models.CharField(max_length=50,null=True)
    release_date = models.DateField()
    image = models.ImageField(upload_to='albums_images', null=True, blank=True)

class Tracks(models.Model):
    track_id = models.AutoField(primary_key=True)
    album_id = models.ForeignKey('Albums', on_delete=models.CASCADE)
    name = models.CharField(max_length=50,null=True)
    path = models.FileField(upload_to='music',null=True)
    playlists_tr = models.ManyToManyField('Playlists',through='Playlist_Tracks')



class Playlists(models.Model):
    playlist_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=50,null=True)
    image = models.ImageField(upload_to='playlist_images',null=True,blank=True)
    tracks_pl = models.ManyToManyField('Tracks',through='Playlist_Tracks')


class Playlist_Tracks(models.Model):
    playlist_id = models.ForeignKey('Playlists', on_delete=models.CASCADE)
    track_id = models.ForeignKey('Tracks', on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['playlist_id', 'track_id'], name='unique_track_playlist'),
        ]
# CREATE TABLE Playlist_Tracks (
#   Playlist_ID INT,
#   Track_ID INT,
#   `Order` INT,
#   PRIMARY KEY (Playlist_ID, Track_ID),
#   FOREIGN KEY (Playlist_ID) REFERENCES Playlists(Playlist_ID),
#   FOREIGN KEY (Track_ID) REFERENCES Tracks(Track_ID)
# );
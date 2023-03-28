from django.contrib import admin
from .models import *


@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    list_display = ('id','name','artist','active')
   
@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('id','psevdo_name')

@admin.register(FavoriteMusic)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user','music')

@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('user_id','playlist_id')

@admin.register(Playlist_Track)
class Playlist_trackAdmin(admin.ModelAdmin):
    list_display = ('playlist_id','music_id')
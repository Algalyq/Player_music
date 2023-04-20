from django.contrib import admin
from .models import * 


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('artist_id','name','genre')


@admin.register(Albums)
class AlbumsAdmin(admin.ModelAdmin):
    list_display = ('album_id','artist_id','name','release_date')


@admin.register(Tracks)
class TracksAdmin(admin.ModelAdmin):
    list_display = ('track_id','album_id','name')


@admin.register(Playlists)
class PlaylistsAdmin(admin.ModelAdmin):
    list_display = ('playlist_id','user_id','name')


@admin.register(Playlist_Tracks)
class PlaylistTracksAdmin(admin.ModelAdmin):
    list_display = ('playlist_id','track_id')
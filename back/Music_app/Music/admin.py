from django.contrib import admin
from .models import *


@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    list_display = ('id','name','artist','active')
   
@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('id','psevdo_name')

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('id','music','color')

@admin.register(FavoriteMusic)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user','music')
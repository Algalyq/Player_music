from django.contrib import admin

# Register your models here.

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
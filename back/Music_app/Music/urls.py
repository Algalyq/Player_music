
from django.contrib import admin
from django.urls import path,include
from .views import *


music_list = MusicsView.as_view({'get':'list','post':'create'})

urlpatterns = [
    path('',music_list,name="all_musics"),
    path('fav/',FavoriteView.as_view(),name="fav"),
    path('v1/',SearchingViewMusic.as_view(),name="searching"),
    path('pl/',PlaylistView.as_view(),name="playlist")
]
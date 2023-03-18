
from django.contrib import admin
from django.urls import path,include
from .views import *


music_list = MusicsView.as_view({'get':'list','post':'create'})

urlpatterns = [
    path('',music_list,name="all_musics")
]

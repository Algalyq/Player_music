from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('artist/', ArtistView.as_view()),
    path('artist/<int:pk>/',SingleArtistView.as_view()),

    path('albums/', AlbumsView.as_view()),
    path('albums/<int:pk>',SingleAlbumsView.as_view()),

    path('tracks/',TracksView.as_view()),
    path('track/<int:pk>',SingleTrackView.as_view()),

    
]
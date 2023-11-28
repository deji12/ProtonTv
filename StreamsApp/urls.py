from django.urls import path
from . import views

urlpatterns = [
    path('create-watch-party/<int:movie_id>/', views.create_watch_party_for_movie, name='create-watch-party'),
]
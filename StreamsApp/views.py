from django.shortcuts import render, redirect
from .models import Stream
from django.contrib.auth.models import User
from movieapp.models import *
from django.contrib.auth.decorators import login_required
from AuthenticationApp.models import Profile

@login_required
def create_watch_party_for_movie(request, movie_id):

    get_movie = movie.objects.get(id=movie_id)

    # incerement number of watch parties that a user has created 
    get_profile = Profile.objects.get(user=request.user)
    get_profile.number_of_created_watch_parties +=1 
    get_profile.save()

    # creating a new watch party 
    create_stream = Stream(
        creator=request.user,
        is_movie = True,
        movie = get_movie
    )

    create_stream.save()

    # redirect to watch party page
    return redirect('watch-party', get_movie.name, create_stream.stream_id)
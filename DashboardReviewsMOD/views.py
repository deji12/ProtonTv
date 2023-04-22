from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from movieapp.models import *

@login_required
def Reviews(request):
    if request.user.is_superuser:
        movie_reviews = reviewss.objects.all()
        episode_reviews = episode_review.objects.all()
        num_reviews = 0
        for i in movie_reviews:
            num_reviews+=1
        for j in episode_reviews:
            num_reviews+=1

        context = {
            'reviews': movie_reviews,
            'episode_review': episode_reviews,
            'num_revs':num_reviews,
        }
        return render(request, 'dashboard/reviews.html', context)
    else:
        return redirect('home')
    
@login_required
def DeleteReviewMovies(request, name, movie_name, body):
    if request.user.is_superuser:
        get_user = User.objects.get(username=name)
        get_profile = Profile.objects.get(user=get_user)
        get_movie = movie.objects.get(name=movie_name)
        get_movie  = reviewss.objects.get(name=get_user, movie=get_movie, body=body)
        get_movie.delete()
        get_profile.reviews -=1
        get_profile.save()
        return redirect('reviews')
    else:
        return redirect('home')

@login_required
def DeleteReviewSeries(request, name, title, series_name, comment_content):
    if request.user.is_superuser:
        get_user = User.objects.get(username=name)
        get_profile = Profile.objects.get(user=get_user)
        get_series = series.objects.get(name=series_name)
        get_episode = episode.objects.get(title=title, series_name=get_series)
        get_episode_comment = episode_review.objects.get(name=get_user, episode=get_episode, series_name=get_series, body=comment_content)
        get_episode_comment.delete()
        get_profile.reviews -=1
        get_profile.save()
        return redirect('reviews')
    else:
        return redirect('home')
    
@login_required   
def FilterReviews(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            search_val = request.POST.get('search')

            user = User.objects.get(username=search_val)
            movie_reviews = reviewss.objects.filter(name=user)
            episode_reviews = episode_review.objects.filter(name=user)
            num_reviews = 0
            for i in movie_reviews:
                num_reviews+=1
            for j in episode_reviews:
                num_reviews+=1

            context = {
                'reviews': movie_reviews,
                'episode_review': episode_reviews,
                'num_revs':num_reviews,
            }
            return render(request, 'dashboard/reviews.html', context)
    else:
        return redirect('home')
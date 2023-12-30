from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from movieapp.models import *
from SeriesApp.models import episode_comment,episode
from AuthenticationApp.models import Profile

@login_required
def Comments(request):
    if request.user.is_superuser:
        series_comment = episode_comment.objects.all()
        movie_comment = comment.objects.all()
        context = {
            'series': series_comment,
            'movie': movie_comment,
        }
        return render(request, 'dashboard/comments.html', context)
    
    return redirect('home')

@login_required
def DeleteCommentSeries(request, name, title, series_name, comment_content, email):
    if request.user.is_superuser:
        get_user = User.objects.get(username=name)
        get_profile = Profile.objects.get(user=get_user)
        get_series = series.objects.get(name=series_name)
        get_episode = episode.objects.get(title=title, series_name=get_series)
        get_episode_comment = episode_comment.objects.get(name=get_user, episode=get_episode, series_name=get_series, body=comment_content)
        get_episode_comment.delete()
        get_profile.comments -=1
        get_profile.save()
        return redirect('comments')
    else:
        return redirect('home')
    
@login_required
def DeleteCommentMovies(request, name, movie_name, body):
    if request.user.is_superuser:
        get_user = User.objects.get(username=name)
        get_profile = Profile.objects.get(user=get_user)
        get_movie = movie.objects.get(name=movie_name)
        get_movie  = comment.objects.get(name=get_user, movie=get_movie,  body=body)
        get_movie.delete()
        get_profile.comments -=1
        get_profile.save()
        return redirect('comments')
    else:
        return redirect('home')
    
@login_required
def FilterCommentsSeries(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            search_val = request.POST.get('search')
            user = User.objects.get(username=search_val)
            series_comment = episode_comment.objects.filter(name=user)
            movie_comment = comment.objects.filter(name=user)
            context = {
                    'series': series_comment,
                    'movie': movie_comment,
                    'search': search_val,
                }
            return render(request, 'dashboard/comments.html', context)
    return redirect('home')
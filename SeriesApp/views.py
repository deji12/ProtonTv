from django.shortcuts import render, redirect
from movieapp.models import *
from Globals.models import *
from SeriesApp.models import *
from SeriesApp.models import episode_review as er
from django.contrib import messages
from AuthenticationApp.models import Profile
from django.core.paginator import Paginator

def Series(request):

    get_series = series.objects.filter(category='series').order_by('-series_air_date')
    category = Category.objects.all()
    get_rate = rate.objects.all()
    get_year = year.objects.all()

    p = Paginator(get_series, 10)
    page = request.GET.get('page')
    page_series = p.get_page(page)

    if request.method == 'POST':
        genre = request.POST.get('check')
        yearr = request.POST.get('year')
        

          # FILTER FOR GENRE AND DATE
        if genre:
            check_genre = Category.objects.get(cat=genre)

            filter_series_obj = series.objects.filter(category='series', genre=check_genre).order_by('-series_air_date')
            
            if yearr:
                filter_series_obj.filter(year_range=yearr)
                    

            p = Paginator(filter_series_obj, 10)
            page = request.GET.get('page')
            page_series = p.get_page(page)

            context = {
                'movies': filter_series_obj,
                'pages': page_series,
                'category': category,
                'rate': get_rate,
                'year': get_year
            }
            return render(request, 'movieapp/series.html', context)
                
        elif yearr:
            filter_series_obj = series.objects.filter(category='series', year_range=yearr).order_by('-series_air_date')
    

            p = Paginator(filter_series_obj, 10)
            page = request.GET.get('page')
            page_series = p.get_page(page)

            context = {
                'movies': filter_series_obj,
                'pages': page_series,
                'category': category,
                'rate': get_rate,
                'year': get_year
            }
                        # return redirect('cat1')   
            return render(request, 'movieapp/series.html', context)

    context = {
        'movies': get_series ,
        'pages': page_series,
        'category': category,
        'rate': get_rate,
        'year': get_year
    }
    return render(request, 'movieapp/series.html', context)

def Anime(request):

    '''
        This view is responsible for displaying the 
        detail page of an anime along with the details of that
        series (seasons, episodes, comments, reviews, etc)
    '''

    get_anime = series.objects.filter(category='anime').order_by('-series_air_date')
    category = Category.objects.all()
    get_rate = rate.objects.all()
    get_year = year.objects.all()

    p = Paginator(get_anime, 10)
    page = request.GET.get('page')
    page_series = p.get_page(page)

    if request.method == 'POST':
        genre = request.POST.get('check')
        yearr = request.POST.get('year')

        check_genre = Category.objects.filter(cat=genre)

          # FILTER FOR GENRE AND DATE
        if genre:

            check_genre = Category.objects.get(cat=genre)

            filter_anime_obj = series.objects.filter(category='anime', genre=check_genre).order_by('-series_air_date')

            if yearr:
                filter_anime_obj.filter(year_range=yearr)

            p = Paginator(filter_anime_obj, 10)
            page = request.GET.get('page')
            page_series = p.get_page(page)
                  
            context = {
                'movies': filter_anime_obj,
                'pages': page_series,
                'category': category,
                'rate': get_rate,
                'year': get_year
            }
            return render(request, 'movieapp/catalog2.html', context)

        elif yearr:
            filter_anime_obj = series.objects.filter(category='anime', year_range=yearr).order_by('-series_air_date')
            
            p = Paginator(filter_anime_obj, 10)
            page = request.GET.get('page')
            page_series = p.get_page(page)

            context = {
                'movies': filter_anime_obj,
                'pages': page_series,
                'category': category,
                'rate': get_rate,
                'year': get_year
            }
                        # return redirect('cat1')   
            return render(request, 'movieapp/anime.html', context)

    context = {
        'movies': get_anime ,
        'pages': page_series,
        'category': category,
        'rate': get_rate,
        'year': get_year
    }
    return render(request, 'movieapp/anime.html', context)

def series_detail(request, name):
    get_series = series.objects.get(name=name)
    get_season = season.objects.get(season_num='1', series_name=get_series)
    first_episode = episode.objects.get(series_name=get_series, season_val=get_season, episode_num='1')
    get_seasons = season.objects.filter(series_name=get_series)
    get_episodes = episode.objects.filter(series_name=get_series)

    # for i in get_seasons:
    #     get_episodes_for_display = episode.objects.filter(series_name=get_series, season_val=i)
    get_episodes_for_display = episode.objects.filter(series_name=get_series).order_by('episode_num')

    fi = 0
    for i in get_episodes:
        fi+=1
    
    get_series.clicks +=1
    get_series.save()

    if get_series.category == 'series':
    
        filtered_series = series.objects.filter(genre__in=get_series.genre.all()).order_by('-series_air_date')[:6]

        context = {
        'series': get_series,
        'first_epi': first_episode,
        'season': get_seasons,
        'epi': fi,
        'episodes': get_episodes_for_display,
        'related_series': filtered_series,
        }
        return render(request, 'movieapp/details2.html', context)
    
    else:
        filtered_series = series.objects.filter(genre__in=get_series.genre.all(), category='anime').order_by('-series_air_date')[:6]
        
        context = {
        'series': get_series,
        'first_epi': first_episode,
        'season': get_seasons,
        'epi': fi,
        'episodes': get_episodes_for_display,
        'related_series': filtered_series,
        }
        return render(request, 'movieapp/details2.html', context)
    
def series_detail_epi(request, name, seasons ,epi):
    get_series = series.objects.get(name=name)
    get_season = season.objects.get(season_num='1', series_name=get_series)
    first_episode = episode.objects.get(series_name=get_series, season_val=get_season, episode_num='1')
    get_seasons = season.objects.filter(series_name=get_series)
    get_episodes = episode.objects.filter(series_name=get_series)

    get_episodes_for_display = episode.objects.filter(series_name=get_series).order_by('episode_num')

    get_series_for_episode = series.objects.get(name=name)

    split_season = seasons.split("|")[1]
    season_number = split_season.split(" ")[2]

    season_for_episode = season.objects.get(series_name=get_series, season_num=season_number)
    _episode = episode.objects.get(series_name=get_series_for_episode, title=epi, season_val=season_for_episode)

    if request.method == 'POST':
        if request.user.is_authenticated:
            get_profile = Profile.objects.get(user=request.user)
            com = request.POST.get('text')
            rev = request.POST.get('review')
            msg = request.POST.get('msg')
            rate = request.POST.get('rate')

            if rev:
                new_epi_review = er(name=request.user, body=msg, title=rev, rate=rate)
                new_epi_review.series_name = get_series_for_episode
                new_epi_review.episode = episode.objects.get(title=epi, series_name=get_series_for_episode)
                new_epi_review.save()
                get_profile.reviews +=1
                get_profile.save()
            elif com:
                new_epi_comment = episode_comment(name=request.user, body=com)
                new_epi_comment.series_name = get_series_for_episode
                new_epi_comment.episode = episode.objects.get(title=epi, series_name=get_series_for_episode)
                new_epi_comment.save()
                get_profile.comments +=1
                get_profile.save()
        else:
            messages.error(request, 'Please signin to post a comment or review')
            return redirect('series-detail-epi', name=name, seasons=seasons, epi=epi)

    
    get_episode_comments = episode_comment.objects.filter(episode = _episode, series_name=get_series_for_episode)
    get_episode_reviews = er.objects.filter(episode = _episode, series_name=get_series_for_episode)

    number_of_episodes = 0
    for i in get_episodes:
        number_of_episodes+=1

    if get_series.category == 'series':
    
        filtered_series = series.objects.filter(genre__in=get_series.genre.all()).order_by('-series_air_date')[:6]

        context = {
            'series': get_series,
            'first_epi': first_episode,
            'season': get_seasons,
            'number_of_episodes': number_of_episodes,
            'episodes': get_episodes_for_display,
            'episode':_episode,
            'comments': get_episode_comments,
            'reviews': get_episode_reviews,
            'related_series': filtered_series,
        }
        return render(request, 'movieapp/epi.html', context)
    
    else:
        filtered_series = series.objects.filter(genre__in=get_series.genre.all()).order_by('-series_air_date')[:6]

        context = {
            'series': get_series,
            'first_epi': first_episode,
            'season': get_seasons,
            'number_of_episodes': number_of_episodes,
            'episodes': get_episodes_for_display,
            'episode': _episode,
            'comments': get_episode_comments,
            'reviews': get_episode_reviews,
            'related_series': filtered_series,
        }
        return render(request, 'movieapp/epi.html', context)
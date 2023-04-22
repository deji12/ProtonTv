from django.shortcuts import render, redirect
from movieapp.models import *
from Globals.models import *
from SeriesApp.models import *
from SeriesApp.models import episode_review as er
from django.contrib import messages

def Series(request):

    '''
        This view is responsible for displaying the 
        detail page of a series along with the details of that
        series (seasons, episodes, comments, reviews, etc)
    '''

    get_movies = series.objects.filter(category='series').order_by('-series_air_date')
    cats = Category.objects.all()
    get_rate = rate.objects.all()
    get_year = year.objects.all()

    if request.method == 'POST':
        gen = request.POST.get('check')
        yearr = request.POST.get('year')

        check_genre = Category.objects.filter(cat=gen)
        fin = None

          # FILTER FOR GENRE AND DATE
        if gen:

            if check_genre:
                fin = Category.objects.get(category=gen)

            genre_1 = series.objects.filter(category='series', genre1=fin).order_by('-series_air_date')
            genre_2 = series.objects.filter(category='series', genre2=fin).order_by('-series_air_date')

            
            if genre_1:
                if yearr:
                    return_result = series.objects.filter(category='series', genre1=fin, year_range=yearr).order_by('-series_air_date')
                    
                    context = {
                        'movies': return_result,
                        'category': cats,
                        'rate': get_rate,
                        'year': get_year
                    }
                    return render(request, 'movieapp/catalog2.html', context)
                else:
                    return_result = series.objects.filter(category='series', genre1=fin).order_by('-series_air_date')
                    context = {
                        'movies': return_result,
                        'category': cats,
                        'rate': get_rate,
                        'year': get_year
                    }
                    return render(request, 'movieapp/catalog2.html', context)  

            elif genre_2:
                if yearr:
                    return_result = series.objects.filter(category='series', genre2=fin, year_range=yearr).order_by('-series_air_date')
                    
                    context = {
                        'movies': return_result,
                        'category': cats,
                        'rate': get_rate,
                        'year': get_year
                    }
                    return render(request, 'movieapp/catalog2.html', context)
                else:
                    return_result = series.objects.filter(category='series', genre2=fin).order_by('-series_air_date')
                    context = {
                        'movies': return_result,
                        'category': cats,
                        'rate': get_rate,
                        'year': get_year
                    }
                        # return redirect('cat1')   
                    return render(request, 'movieapp/catalog2.html', context)

        if yearr:
            get_movies_by_year = series.objects.filter(category='series', year_range=yearr).order_by('-series_air_date')
            context = {
                'movies': get_movies_by_year,
                'category': cats,
                'rate': get_rate,
                'year': get_year
            }
                        # return redirect('cat1')   
            return render(request, 'movieapp/series.html', context)

    context = {
        'movies': get_movies ,
        'category': cats,
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

    get_movies = series.objects.filter(category='anime').order_by('-series_air_date')
    cats = Category.objects.all()
    get_rate = rate.objects.all()
    get_year = year.objects.all()

    if request.method == 'POST':
        gen = request.POST.get('check')
        yearr = request.POST.get('year')

        check_genre = Category.objects.filter(cat=gen)
        fin = None

          # FILTER FOR GENRE AND DATE
        if gen:

            if check_genre:
                fin = Category.objects.get(cat=gen)

            genre_1 = series.objects.filter(category='anime', genre1=fin).order_by('-series_air_date')
            genre_2 = series.objects.filter(category='anime', genre2=fin).order_by('-series_air_date')

            
            if genre_1:
                if yearr:
                    return_result = series.objects.filter(category='anime', genre1=fin, year_range=yearr).order_by('-series_air_date')
                    
                    context = {
                        'movies': return_result,
                        'category': cats,
                        'rate': get_rate,
                        'year': get_year
                    }
                    return render(request, 'movieapp/catalog2.html', context)
                else:
                    return_result = series.objects.filter(category='anime',genre1=fin).order_by('-series_air_date')
                    context = {
                        'movies': return_result,
                        'category': cats,
                        'rate': get_rate,
                        'year': get_year
                    }
                    return render(request, 'movieapp/catalog2.html', context)  

            elif genre_2:
                if yearr:
                    return_result = series.objects.filter(category='anime', genre2=fin, year_range=yearr).order_by('-series_air_date')
                    
                    context = {
                        'movies': return_result,
                        'category': cats,
                        'rate': get_rate,
                        'year': get_year
                    }
                    return render(request, 'movieapp/catalog2.html', context)
                else:
                    return_result = series.objects.filter(category='anime', genre2=fin).order_by('-series_air_date')
                    context = {
                        'movies': return_result,
                        'category': cats,
                        'rate': get_rate,
                        'year': get_year
                    }
                        # return redirect('cat1')   
                    return render(request, 'movieapp/catalog2.html', context)

        if yearr:
            get_movies_by_year = series.objects.filter(category='anime', year_range=yearr).order_by('-series_air_date')
            context = {
                'movies': get_movies_by_year,
                'category': cats,
                'rate': get_rate,
                'year': get_year
            }
                        # return redirect('cat1')   
            return render(request, 'movieapp/anime.html', context)

    context = {
        'movies': get_movies ,
        'category': cats,
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

    series_genre = get_series.genre1
    series_genre2 = get_series.genre2
    pics = photos.objects.filter(series_name=get_series)

    if get_series.category == 'series':
    
        filtered_series = series.objects.filter(genre1=series_genre).order_by('-series_air_date')[:2]
        filtered_series2 = series.objects.filter(genre2=series_genre2).order_by('-series_air_date')[:2]

        filtered_series3 = series.objects.filter(genre1=series_genre2).order_by('-series_air_date')[:2]
        filtered_series4 = series.objects.filter(genre2=series_genre2).order_by('-series_air_date')[:2]

        context = {
        'series': get_series,
        'first_epi': first_episode,
        'season': get_seasons,
        'epi': fi,
        'episodes': get_episodes_for_display,
        'dis': filtered_series,
        'dis2': filtered_series2,
        'dis3': filtered_series3,
        'dis4': filtered_series4,
        'pic': pics
        }
        return render(request, 'movieapp/details2.html', context)
    
    else:
        filtered_series = series.objects.filter(genre1=series_genre, category='anime').order_by('-series_air_date')[:2]
        filtered_series2 = series.objects.filter(genre2=series_genre2, category='anime').order_by('-series_air_date')[:2]

        filtered_series3 = series.objects.filter(genre1=series_genre2, category='anime').order_by('-series_air_date')[:2]
        filtered_series4 = series.objects.filter(genre2=series_genre2, category='anime').order_by('-series_air_date')[:2]

        context = {
        'series': get_series,
        'first_epi': first_episode,
        'season': get_seasons,
        'epi': fi,
        'episodes': get_episodes_for_display,
        'dis': filtered_series,
        'dis2': filtered_series2,
        'dis3': filtered_series3,
        'dis4': filtered_series4,
        'pic': pics
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
    part_se = episode.objects.get(series_name=get_series_for_episode, title=epi, season_val=season_for_episode)
    epis = episode.objects.get(series_name=get_series_for_episode, title=epi, season_val=season_for_episode)

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

    
    get_episode_comments = episode_comment.objects.filter(episode = epis, series_name=get_series_for_episode)
    get_episode_reviews = er.objects.filter(episode = epis, series_name=get_series_for_episode)

    fi = 0
    for i in get_episodes:
        fi+=1

    series_genre = get_series.genre1
    
    series_genre2 = get_series.genre2

    pics = photos.objects.filter(series_name=get_series)

    if get_series.cat == 'series':
    
        filtered_series = series.objects.filter(genre1=series_genre).order_by('-series_air_date')[:2]
        filtered_series2 = series.objects.filter(genre2=series_genre2).order_by('-series_air_date')[:2]

        filtered_series3 = series.objects.filter(genre1=series_genre2).order_by('-series_air_date')[:2]
        filtered_series4 = series.objects.filter(genre2=series_genre2).order_by('-series_air_date')[:2]

        context = {
        'series': get_series,
        'first_epi': first_episode,
        'season': get_seasons,
        'epi': fi,
        'episodes': get_episodes_for_display,
        'se': part_se,
        'coms': get_episode_comments,
        'revs': get_episode_reviews,
        'dis': filtered_series,
        'dis2': filtered_series2,
        'dis3': filtered_series3,
        'dis4': filtered_series4,
        'pic': pics
        }
        return render(request, 'movieapp/epi.html', context)
    
    else:
        filtered_series = series.objects.filter(genre1=series_genre, cat='anime').order_by('-series_air_date')[:2]
        filtered_series2 = series.objects.filter(genre2=series_genre2, cat='anime').order_by('-series_air_date')[:2]

        filtered_series3 = series.objects.filter(genre1=series_genre2, cat='anime').order_by('-series_air_date')[:2]
        filtered_series4 = series.objects.filter(genre2=series_genre2, cat='anime').order_by('-series_air_date')[:2]

        context = {
        'series': get_series,
        'first_epi': first_episode,
        'season': get_seasons,
        'epi': fi,
        'episodes': get_episodes_for_display,
        'se': part_se,
        'coms': get_episode_comments,
        'revs': get_episode_reviews,
        'dis': filtered_series,
        'dis2': filtered_series2,
        'dis3': filtered_series3,
        'dis4': filtered_series4,
        'pic': pics
        }
        return render(request, 'movieapp/epi.html', context)

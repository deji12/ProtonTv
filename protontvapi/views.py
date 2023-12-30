from django.shortcuts import render
from rest_framework.decorators import api_view
from movieapp.models import movie, series, photos
from Globals.models import *
from SeriesApp.models import *
from .serializers import *
from rest_framework.response import Response

@api_view(['GET'])
def home(request):
    return Response({
        'To get all movies': f'{request.get_host()}/api/all-movies/',
        'To get a particular movie': f'{request.get_host()}/api/get-movie/movie name/',
        'To get all series': f'{request.get_host()}/api/all-series/',
        'To get a particular series': f'{request.get_host()}/api/get-series/series name/',
        'To get all series seasons':  f'{request.get_host()}/api/all-series-seasons/',
        'To get all series episodes': f'{request.get_host()}/api/all-series-episodes/',
        'To get all genres': f'{request.get_host()}/api/all-genres/',
        'To get all thumbnails': f'{request.get_host()}/api/all-thumbnails/',
    })

@api_view(['GET'])
def Movies(request):
    all_movies = movie.objects.all().order_by('-date_added')
    serializer = GetAllMoviesSerializer(all_movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def Series(request):
    all_series = series.objects.all().order_by('-series_air_date')
    serializer = GetAllSeriesSerializer(all_series, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def Episodes(request):
    all_episodes = episode.objects.all().order_by('-dou')
    serializer = GetAllEpisodesSerializer(all_episodes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def Photos(request):
    all_photos = photos.objects.all()
    serializer = GetAllPhotosSerializer(all_photos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def Photos(request):
    all_photos = season.objects.all()
    serializer = GetAllSeasonsSerializer(all_photos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def Genres(request):
    all_genres = Category.objects.all()
    serializer = GetAllGenresSerializer(all_genres, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def GetMovie(request, name):
    try:
        mov = movie.objects.get(name=name)
        serializer = GetAllMoviesSerializer(mov, many=False)
        return Response(serializer.data)
    except:
        return Response({'Error': f'Movie {name} does not exist in database'})

@api_view(['GET'])
def GetSeries(request, name):
    try:
        serie = series.objects.get(name=name)
        serializer = GetAllSeriesSerializer(serie, many=False)
        return Response(serializer.data)
    except:
        return Response({'Error': f'Series {name}, does not exist in database'})

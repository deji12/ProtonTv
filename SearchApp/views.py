from django.shortcuts import render
from movieapp.models import movie, series

def searchresult(request):

    if request.method == 'POST':
        search = request.POST.get('search')
       
        filter_for_movies = movie.objects.filter(name__icontains=search).order_by('-date_added')
        filter_for_series = series.objects.filter(name__icontains=search).order_by('-series_air_date')


        context = {
                'movie': filter_for_movies,
                'series': filter_for_series,
                'search': search
            }
        return render(request, 'movieapp/search-result.html', context)
    return render(request, 'movieapp/search-result.html')

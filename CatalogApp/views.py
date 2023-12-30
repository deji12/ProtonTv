from django.shortcuts import render
from movieapp.models import Category, rate, year, movie
from django.core.paginator import Paginator

def catalog_grid(request):

    '''
        This view is responsible for
        displaying all movies in a grid form
    '''

    get_movies = movie.objects.filter(draft=False, premier=False).order_by('-date_added')
    category = Category.objects.all()
    get_rate = rate.objects.all()
    get_year = year.objects.all().order_by('-id')

    p = Paginator(get_movies, 18)
    page = request.GET.get('page')
    page_series = p.get_page(page)

    if request.method == 'POST':

        '''
                In this post request, the user 
                can filter for movies by year and genre 
        '''

        genre = request.POST.get('check')
        yearr = request.POST.get('year')

        # FILTER FOR GENRE AND DATE
        if genre:
            check_genre = Category.objects.filter(cat=genre)
            
            filter_movie_obj = movie.objects.filter(genre__in=check_genre, draft=False, premier=False).order_by('-date_added')
            
            if yearr:
                filter_movie_obj.filter(year_range=yearr)

            p = Paginator(filter_movie_obj, 18)
            page = request.GET.get('page')
            page_series = p.get_page(page)

            context = {
                'movies': filter_movie_obj,
                'category': category,
                'pages': page_series,
                'rate': get_rate,
                'year': get_year
            }
            return render(request, 'movieapp/catalog1.html', context)
            
        elif yearr:

            filter_movie_obj = movie.objects.filter(year_range=yearr, draft=False, premier=False).order_by('-date_added')

            p = Paginator(filter_movie_obj, 18)
            page = request.GET.get('page')
            page_series = p.get_page(page)

            context = {
                'movies': filter_movie_obj,
                'category': category,
                'pages': page_series,
                'rate': get_rate,
                'year': get_year
            }
            return render(request, 'movieapp/catalog1.html', context)
    
    context = {
        'movies': get_movies,
        'pages': page_series,
        'category': category,
        'rate': get_rate,
        'year': get_year
    }
    return render(request, 'movieapp/catalog1.html', context)

def catalog_list(request):
    get_movies = movie.objects.filter(draft=False, premier=False).order_by('-date_added')
    category = Category.objects.all()
    get_rate = rate.objects.all()
    get_year = year.objects.all().order_by('-id')

    p = Paginator(get_movies, 18)
    page = request.GET.get('page')
    page_series = p.get_page(page)

    if request.method == 'POST':

        '''
                In this post request, the user 
                can filter for movies by year and genre 
        '''

        genre = request.POST.get('check')
        yearr = request.POST.get('year')

        # FILTER FOR GENRE AND DATE
        if genre:
            check_genre = Category.objects.filter(cat=genre)
            
            filter_movie_obj = movie.objects.filter(genre__in=check_genre, draft=False, premier=False).order_by('-date_added')
            
            if yearr:
                filter_movie_obj.filter(year_range=yearr)

            p = Paginator(filter_movie_obj, 18)
            page = request.GET.get('page')
            page_series = p.get_page(page)
                    
            context = {
                'movies': filter_movie_obj,
                'pages': page_series,
                'category': category,
                'rate': get_rate,
                'year': get_year
            }
            return render(request, 'movieapp/catalog2.html', context)
            
        elif yearr:

            filter_movie_obj = movie.objects.filter(year_range=yearr, draft=False, premier=False).order_by('-date_added')

            p = Paginator(filter_movie_obj, 18)
            page = request.GET.get('page')
            page_series = p.get_page(page)

            context = {
                'movies': filter_movie_obj,
                'pages': page_series,
                'category': category,
                'rate': get_rate,
                'year': get_year
            }
            return render(request, 'movieapp/catalog2.html', context)

    context = {
        'movies': get_movies ,
        'pages': page_series,
        'category': category,
        'rate': get_rate,
        'year': get_year
    }
    return render(request, 'movieapp/catalog2.html', context)
from django.shortcuts import render
from movieapp.models import Category, rate, year, movie

def catalog_grid(request):

    '''
        This view is responsible for
        displaying all movies in a grid form
    '''

    get_movies = movie.objects.all().order_by('-date_added')
    category = Category.objects.all()
    get_rate = rate.objects.all()
    get_year = year.objects.all()

    if request.method == 'POST':

        '''
                In this post request, the user 
                can filter for movies by year and genre 
        '''

        gen = request.POST.get('check')
        yearr = request.POST.get('year')

        check_genre = Category.objects.filter(cat=gen)
        filter_by_genre = None

        # FILTER FOR GENRE AND DATE
        if gen:

            if check_genre:
                filter_by_genre = Category.objects.get(cat=gen)

            genre_1 = movie.objects.filter(genre1=filter_by_genre).order_by('-date_added')
            genre_2 = movie.objects.filter(genre2=filter_by_genre).order_by('-date_added')

            if genre_1:
                if yearr:
                    return_result = movie.objects.filter(genre1=filter_by_genre, year_range=yearr).order_by('-date_added')
                    
                    context = {
                        'movies': return_result,
                        'category': category,
                        'rate': get_rate,
                        'year': get_year
                    }
                    return render(request, 'movieapp/catalog1.html', context)
                else:
                    return_result = movie.objects.filter(genre1=filter_by_genre).order_by('-date_added')
                    context = {
                        'movies': return_result,
                        'category': category,
                        'rate': get_rate,
                        'year': get_year
                    }
                    return render(request, 'movieapp/catalog1.html', context)  

            elif genre_2:
                if yearr:
                    return_result = movie.objects.filter(genre2=filter_by_genre, year_range=yearr).order_by('-date_added')
                    
                    context = {
                        'movies': return_result,
                        'category': category,
                        'rate': get_rate,
                        'year': get_year
                    }
                    return render(request, 'movieapp/catalog1.html', context)
                else:
                    return_result = movie.objects.filter(genre2=filter_by_genre).order_by('-date_added')
                    context = {
                        'movies': return_result,
                        'category': category,
                        'rate': get_rate,
                        'year': get_year
                    }
                    return render(request, 'movieapp/catalog1.html', context)
              
        if yearr:
            get_movies_by_year = movie.objects.filter(year_range=yearr).order_by('-date_added')
            context = {
                'movies': get_movies_by_year,
                'category': category,
                'rate': get_rate,
                'year': get_year
            }
            return render(request, 'movieapp/catalog1.html', context)
   
    context = {
        'movies': get_movies,
        'category': category,
        'rate': get_rate,
        'year': get_year
    }
    return render(request, 'movieapp/catalog1.html', context)

def catalog_list(request):
    get_movies = movie.objects.all().order_by('-date_added')
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

            genre_1 = movie.objects.filter(genre1=fin).order_by('-date_added')
            genre_2 = movie.objects.filter(genre2=fin).order_by('-date_added')

            if genre_1:
                if yearr:
                    return_result = movie.objects.filter(genre1=fin, year_range=yearr).order_by('-date_added')
                    
                    context = {
                        'movies': return_result,
                        'category': cats,
                        'rate': get_rate,
                        'year': get_year
                    }
                    return render(request, 'movieapp/catalog2.html', context)
                else:
                    return_result = movie.objects.filter(genre1=fin).order_by('-date_added')
                    context = {
                        'movies': return_result,
                        'category': cats,
                        'rate': get_rate,
                        'year': get_year
                    }
                    return render(request, 'movieapp/catalog2.html', context)  

            elif genre_2:
                if yearr:
                    return_result = movie.objects.filter(genre2=fin, year_range=yearr).order_by('-date_added')
                    
                    context = {
                        'movies': return_result,
                        'category': cats,
                        'rate': get_rate,
                        'year': get_year
                    }
                    return render(request, 'movieapp/catalog2.html', context)
                else:
                    return_result = movie.objects.filter(genre2=fin).order_by('-date_added')
                    context = {
                        'movies': return_result,
                        'category': cats,
                        'rate': get_rate,
                        'year': get_year
                    }
                        # return redirect('cat1')   
                    return render(request, 'movieapp/catalog2.html', context)
              
        if yearr:
            get_movies_by_year = movie.objects.filter(year_range=yearr).order_by('-date_added')
            context = {
                'movies': get_movies_by_year,
                'category': cats,
                'rate': get_rate,
                'year': get_year
            }
                        # return redirect('cat1')   
            return render(request, 'movieapp/catalog2.html', context)

    context = {
        'movies': get_movies ,
        'category': cats,
        'rate': get_rate,
        'year': get_year
    }
    return render(request, 'movieapp/catalog2.html', context)
from django.shortcuts import render, redirect
from django.contrib import messages
from movieapp.models import *
from AuthenticationApp.models import Profile

def detail(request, name):

    '''
        This view is responsible for 
        displaying the detail page of a 
        movie as well as the contents of 
        that movie.
    '''

    get_movie = movie.objects.get(name=name)

    # check if user submits a comment or review
    if request.method == 'POST':
        if request.POST.get('current_video_watch_percentage') and request.POST.get('increment') == True:
            # get_movie.watch_hours += 10
            # get_movie.save()
            print('------------------yesssss')
        
        if request.user.is_authenticated: # check if user is logged in
            get_profile = Profile.objects.get(user=request.user)
            title = request.POST.get('title')
            review = request.POST.get('review')
            text = request.POST.get('body')
            rate = request.POST.get('rate')

            if text:  # means user filled the comment form
                # creating a new comment and saving it
                new_comment = comment(name=request.user, body=text)
                new_comment.movie = movie.objects.get(name=name)
                new_comment.save()
                get_profile.comments +=1 # incrementing the number of comments the user has on this website by 1
                get_profile.save()
                return redirect('detail', name=name)
            if title: # means user filled review form
                # creating a new review object and saving it
                new_review = reviewss(name=request.user, title=title, body=review, rate=rate)
                new_review.movie = movie.objects.get(name=name)
                get_profile.reviews +=1  # incrementing the number of reviews the user has on this website by 1
                get_profile.save()
                new_review.save()
                return redirect('detail', name=name)
        else:  # return an error prompting that user has to be logged in to comment or give a review
            messages.error(request, 'Please signin to post a comment or review')
            return redirect('detail', name=name)    

    
    get_movie.clicks +=1 # increment the number of clicks by 1
    get_movie.save()

    pics = photos.objects.filter(movie_name=get_movie)  # get pictures associated with movie
    all_coms = comment.objects.filter(movie=get_movie) # get all comments associated with movie
    all_reviews = reviewss.objects.filter(movie=get_movie) # get all series associated with movie

    all_movies = movie.objects.all()
    movie_genre = get_movie.genre1
    movie_genre2 = get_movie.genre2


    '''
        Here, we search for other movies that have similar
        categories with the selected movie in detail page
    '''

    if get_movie.category == 'anime': # check if movie category is anime
        # filtering to get other anime's that have similar category
        filtered_movie = movie.objects.filter(category='anime', genre1=movie_genre).order_by('-date_added')[:2]
        filtered_movie2 = movie.objects.filter(category='anime', genre2=movie_genre2).order_by('-date_added')[:2]

        filtered_movie3 = movie.objects.filter(category='anime', genre1=movie_genre2).order_by('-date_added')[:2]
        filtered_movie4 = movie.objects.filter(category='anime', genre2=movie_genre).order_by('-date_added')[:2]

        # returning data
        context = {
            'movie': get_movie,
            'al': all_movies,
            'coms': all_coms,
            'revs': all_reviews,
            'dis': filtered_movie,
            'dis2': filtered_movie2,
            'dis3': filtered_movie3,
            'dis4': filtered_movie4,
            'pics': pics,
        }
        return render(request, 'movieapp/details1.html', context)

    else: # if movie is not anime
        # filtering to get other movies that have similar category
        filtered_movie = movie.objects.filter(category='movie', genre1=movie_genre).order_by('-date_added')[:2]
        filtered_movie2 = movie.objects.filter(category='movie', genre2=movie_genre).order_by('-date_added')[:2]

        filtered_movie3 = movie.objects.filter(category='movie', genre1=movie_genre2).order_by('-date_added')[:2]
        filtered_movie4 = movie.objects.filter(category='movie', genre2=movie_genre2).order_by('-date_added')[:2]

        #returning context
        context = {
            'movie': get_movie,
            'al': all_movies,
            'coms': all_coms,
            'revs': all_reviews,
            'dis': filtered_movie,
            'dis2': filtered_movie2,
            'dis3': filtered_movie3,
            'dis4': filtered_movie4,
            'pics': pics,
        }
        return render(request, 'movieapp/details1.html', context)
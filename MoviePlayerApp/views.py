from django.shortcuts import render, redirect
from django.contrib import messages
from movieapp.models import *
from AuthenticationApp.models import Profile
from StreamsApp.models import Stream
from django.contrib.auth.decorators import login_required

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
                new_review.save()

                get_profile.reviews +=1  # incrementing the number of reviews the user has on this website by 1
                get_profile.save()

                return redirect('detail', name=name)
        else:  # return an error prompting that user has to be logged in to comment or give a review
            messages.error(request, 'Please signin to post a comment or review')
            return redirect('detail', name=name)    

    else:
        get_movie.clicks +=1 # increment the number of clicks by 1
        get_movie.save()


    '''
        Here, we search for other movies that have similar
        categories with the selected movie in detail page
    '''

    if get_movie.category == 'anime': # check if movie category is anime
        # filtering to get other anime's that have similar category
        filtered_movie = movie.objects.filter(category='anime', genre__in=get_movie.genre.all()).distinct().exclude(id=get_movie.id).order_by('-date_added')[:6]

        # returning data
        context = {
            'movie': get_movie,
            'related_movies': filtered_movie,
        }
        return render(request, 'movieapp/details1.html', context)

    else: # if movie is not anime
        # filtering to get other movies that have similar category
        filtered_movie = movie.objects.filter(category='movie', genre__in=get_movie.genre.all()).distinct().exclude(id=get_movie.id).order_by('-date_added')[:6]

        #returning context
        context = {
            'movie': get_movie,
            'related_movies': filtered_movie,
        }
        return render(request, 'movieapp/details1.html', context)
    

@login_required
def MovieStreamDetail(request, name, stream_id):

    '''
        This view is responsible for 
        displaying the detail page of a 
        movie as well as the contents of 
        that movie for watch parties.
    '''

    stream_object = None

    try:
        stream_object = Stream.objects.get(stream_id=stream_id)
    except Stream.DoesNotExist:
        messages.error(request, f"Watch party with id: '{stream_id}' does not exist")
        return redirect('watch-party', name=name, stream_id=stream_id)

    get_movie = movie.objects.get(name=name)

    # check if user submits a comment or review
    if request.method == 'POST':
        
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

    else:
        get_movie.clicks +=1 # increment the number of clicks by 1
        get_movie.save()


    '''
        Here, we search for other movies that have similar
        categories with the selected movie in detail page
    '''

    if get_movie.category == 'anime': # check if movie category is anime
        # filtering to get other anime's that have similar category
        filtered_movie = movie.objects.filter(category='anime', genre__in=get_movie.genre.all()).distinct().exclude(id=get_movie.id).order_by('-date_added')[:6]

        # returning data
        context = {
            'movie': get_movie,
            'related_movies': filtered_movie,
            'stream': stream_object
        }
        return render(request, 'movieapp/detail.html', context)

    else: # if movie is not anime
        # filtering to get other movies that have similar category
        filtered_movie = movie.objects.filter(category='movie', genre__in=get_movie.genre.all()).distinct().exclude(id=get_movie.id).order_by('-date_added')[:6]

        #returning context
        context = {
            'movie': get_movie,
            'related_movies': filtered_movie,
            'stream': stream_object
        }
        return render(request, 'StreamsApp/detail.html', context)
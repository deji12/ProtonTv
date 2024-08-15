from django.shortcuts import render
from .models import movie, series
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings

def home(request):

    ''' Returning movies, series, and anime
    to the frontend'''

    # filtering to get movies, series, and anime from database
    get_movies = movie.objects.filter(new=True).order_by('-date_added')[:64]
    get_series = series.objects.filter(is_series_new=True, draft=False, premier=False).order_by('-series_air_date')[:34]
    get_anime = series.objects.filter(category='anime', is_series_new=True, draft=False, premier=False).order_by('-series_air_date')[:34]
    get_anime_movie = movie.objects.filter(category='anime', new=True).order_by('-date_added')[:34]

    #getting movies and series set as premier
    get_premier = movie.objects.filter(premier=True).order_by('-date_added')[:3]
    get_premier_series = series.objects.filter(premier=True).order_by('-series_air_date')[:3]

    #returning querysets to the frontend
    context = {
        'movie': get_movies,
        'series': get_series,
        'anime': get_anime,
        'movie_anime': get_anime_movie,
        'premier': get_premier,
        'series_premier': get_premier_series,
    }
    return render(request, 'movieapp/index.html', context)


def pricing(request):
    return render(request, 'movieapp/pricing.html', {})

def faq(request):
    return render(request, 'movieapp/faq.html', {})

def about(request):
    return render(request, 'movieapp/about.html', {})

def privacy(request):
    return render(request, 'movieapp/privacy.html',{})

def contacts(request):

    '''
        The contact view collects
        a users name, email, body,
        and subject and sends it to the admin of the website 
        via email.
    '''

    if request.method == 'POST':
        # retrieving user input after form submition
        name = request.POST['name']
        email = request.POST['email']
        sub = request.POST['subject']
        body  = request.POST['text']


        # sending email with email message library
        email_message = EmailMessage (
                f'ProtonTv: {sub}',
                f'From: {name} \n \n Email: {email} \n \n Body: {body}',
                settings.EMAIL_HOST_USER,
                ['theprotonguy@yahoo.com']
            )
        email_message.fail_silently = True
        email_message.send()

        messages.success(request, 'Thank you for contacting us. We will reply shortly')
        return render(request, 'movieapp/contacts.html', {})
    
    return render(request, 'movieapp/contacts.html', {})
    

def NotFound(request, exception):
    return render(request, 'movieapp/404.html', {})


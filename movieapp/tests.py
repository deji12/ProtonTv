from django.test import TestCase

import requests
# from .models import movie

MOVIE_ENDPOINT = 'https://vidsrc.to/vapi/movie'
TYPE_PARAM = 'new'
page_param = 1

def get_movies():


    api_url = f'{MOVIE_ENDPOINT}/{TYPE_PARAM}/{page_param if page_param else ""}'

    try:
        response = requests.get(api_url)
        response.raise_for_status()  
        data = response.json()
        print(data['result']['items'])
    except requests.exceptions.RequestException as e:
        print('There was a problem with the request:', e)

test = '2021-'
if '-' in test:
    print('yes')
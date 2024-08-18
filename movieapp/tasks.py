from __future__ import absolute_import, unicode_literals
from movie.celery import app
from celery.utils.log import get_task_logger
import requests
from .models import movie, YEAR_RANGES
from Globals.models import Category, Country
import re
from django.db import transaction

logger = get_task_logger(__name__)

MOVIE_ENDPOINT = 'https://vidsrc.xyz/movies/latest'
TYPE_PARAM = 'new'
KEY = '8d822da1'
pattern = r'\s\d{4}$'

@app.task(name='scrape_movies')
def get_movies():
    page_param = 1

    while page_param <= 20:
        api_url = f'{MOVIE_ENDPOINT}/page-{page_param}.json'

        try:
            response = requests.get(api_url)
            data = response.json()

            print('-> Getting movies')

            for i in data['result']:
                _title = i['title']
                title = re.sub(pattern, '', _title)

                if title == "Jackpot!":
                    continue

                if not movie.objects.filter(name=title, imdb_id=i['imdb_id']).exists():
                    omdb_endpoint = f"http://www.omdbapi.com/?apikey={KEY}&t={title}"
                    omdb_response = requests.get(omdb_endpoint)

                    omdb_response_data = omdb_response.json()

                    if omdb_response_data['Response'] != 'False':
                        year_str = omdb_response_data['Year']
                        year = re.sub(r'[^0-9]', '', year_str)

                        if not year:
                            continue  # Skip if the year is empty after cleaning

                        # Ensure atomicity
                        with transaction.atomic():
                            create_new_movie = movie(
                                name=title,
                                video=i['embed_url'],
                                imdb_id=i['imdb_id'],
                                category='movie'
                            )

                            create_new_movie.year = year
                            create_new_movie.duration = omdb_response_data['Runtime'] if omdb_response_data['Runtime'] else None
                            create_new_movie.info = omdb_response_data['Plot']
                            create_new_movie.thumbnail_url = omdb_response_data['Poster']
                            create_new_movie.rating = omdb_response_data['imdbRating']
                            create_new_movie.new = True
                            create_new_movie.rated = omdb_response_data['Rated']

                            genre_names = omdb_response_data['Genre'].split(',')
                            country_names = omdb_response_data['Country'].split(',')

                            year_range = None
                            for range_choice, _ in YEAR_RANGES:
                                start_year, end_year = map(int, range_choice.split('-'))
                                if start_year <= int(year) <= end_year:
                                    create_new_movie.year_range = range_choice
                                    break

                            create_new_movie.save()

                            for country_name in country_names:
                                country, created = Country.objects.get_or_create(name=country_name)
                                create_new_movie.country.add(country)

                            for genre_name in genre_names:
                                genre_name = genre_name.strip().upper()
                                genre, created = Category.objects.get_or_create(cat=genre_name)
                                create_new_movie.genre.add(genre)

                            create_new_movie.save()

            page_param += 1

        except requests.exceptions.RequestException as e:
            print('There was a problem with the request:', e)

    return "-> Added movies successfully"

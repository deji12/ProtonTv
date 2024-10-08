from rest_framework import serializers
from movieapp.models import *
from SeriesApp.models import *
from Globals.models import *

class GetAllMoviesSerializer(serializers.ModelSerializer):

    genre = serializers.StringRelatedField(many=True)

    class Meta:
        model = movie
        fields = ['name', 'info', 'thumbnail', 'age', 'genre', 'rating', 'year', 'country', 'video', 'duration']

class GetAllSeriesSerializer(serializers.ModelSerializer):
    genre = serializers.StringRelatedField(many=True)
    class Meta:
        model = series
        fields = ['name', 'info', 'thumbnail', 'age', 'genre', 'rating', 'year', 'country']

class GetAllEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = episode
        fields = ['title', 'series_name', 'season_val', 'episode_num', 'video', 'duration']

class GetAllPhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = photos
        fields = '__all__'      

class GetAllSeasonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = season
        fields = ['id', 'season_num', 'series_name']


class GetAllGenresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__' 
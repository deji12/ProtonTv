from django.db import models
from django.contrib.auth.models import User
from SeriesApp.models import series
from Globals.models import *

class movie(models.Model):
    name = models.CharField(max_length=20000)
    info = models.TextField()
    video = models.CharField(max_length=10000, null=True, blank=True)

    sub_title_language = models.CharField(max_length=225, null=True, blank=True)
    srclanguage = models.CharField(max_length=225, blank=True, null=True)
    sub_title_file = models.CharField(max_length=1000, null=True, blank=True)

    sub_title_language2 = models.CharField(max_length=225, null=True, blank=True)
    srclanguage2 = models.CharField(max_length=225, blank=True, null=True)
    sub_title_file2 = models.CharField(max_length=1000, null=True, blank=True)

    thumbnail = models.FileField(upload_to='thumb/')
    age = models.CharField(default=13, max_length=20)
    category = models.CharField(default='cartoon', max_length=200)
    premier = models.BooleanField(default=False)
    genre = models.ManyToManyField(Category, related_name='category', null=True, blank=True)
    rating = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    year_range = models.CharField(max_length=200, null=True, blank=True)
    new = models.BooleanField(default=False)
    duration = models.CharField(max_length=100)
    country = models.CharField(max_length=200)
    draft = models.BooleanField(default=False)
    date_added = models.DateField(auto_now_add=True, null=True, blank=True)
    clicks = models.IntegerField(null=True, blank=True, default=0)
    watch_hours = models.FloatField(default=0.0)

    def __str__(self):
        return self.name
    
    def return_movie_comments(self):

        return comment.objects.filter(movie=self).order_by('-date')
    
    def return_movie_reviews(self):

        return reviewss.objects.filter(movie=self).order_by('-date')
    
    def return_movie_pictures(self):

        return photos.objects.filter(movie_name=self)

class comment(models.Model):
    movie = models.ForeignKey(movie, related_name='movie_comment', on_delete=models.CASCADE)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.movie)

class reviewss(models.Model):
    movie = models.ForeignKey(movie, related_name='movie_review', on_delete=models.CASCADE)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=5000)
    body = models.TextField()
    rate = models.IntegerField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.movie)

class photos(models.Model):
    series_name = models.ForeignKey(series, on_delete=models.CASCADE, null=True, blank=True)
    movie_name = models.ForeignKey(movie, on_delete=models.CASCADE, null=True, blank=True)
    pic = models.FileField(upload_to='movie-photos')

    def __str__(self):
        return str(self.movie_name)
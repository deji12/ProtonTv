from django.db import models
from Globals.models import *
from django.contrib.auth.models import User

class series(models.Model):
    name = models.CharField(max_length=20000)
    info = models.TextField()
    thumbnail = models.FileField(upload_to='thumb/series/')
    age = models.CharField(default=13, max_length=20)
    genre1 = models.ForeignKey(Category, related_name='series_category1', on_delete=models.CASCADE, null=True, blank=True)
    genre2 = models.ForeignKey(Category, related_name='series_category2', on_delete=models.CASCADE, null=True, blank=True)
    rating = models.CharField(max_length=100)
    is_series_new = models.BooleanField(default=False)
    premier = models.BooleanField(default=False)
    series_air_date = models.DateField(auto_now_add=True)
    year_range = models.CharField(max_length=200, null=True, blank=True)
    year = models.CharField(max_length=100)
    country = models.CharField(max_length=200)
    draft = models.BooleanField(default=False)
    clicks = models.IntegerField(null=True, blank=True, default=0)
    category = models.CharField(default='anime', max_length=200)
    watch_hours = models.FloatField(default=0.0)

    def __str__(self):
        return str(self.name)
    
class season(models.Model):
    series_name = models.ForeignKey(series, related_name='season_val', on_delete=models.CASCADE)
    season_num = models.CharField(max_length=100)
    heading = models.CharField(max_length=100, blank=True, null=True)
    collapse = models.CharField(max_length=100, blank=True, null=True)
    

    def __str__(self):
        return str(f'{self.series_name} | Season {self.season_num}')

class episode(models.Model):
    title = models.CharField(max_length=200, default='title')
    series_name = models.ForeignKey(series, related_name='season_epi', on_delete=models.CASCADE)
    season_val = models.ForeignKey(season, related_name='episode', on_delete=models.CASCADE)   
    episode_num = models.IntegerField( default=1) 
    video = models.CharField(max_length=10000, null=True, blank=True)

    sub_title_lang = models.CharField(max_length=225, null=True, blank=True)
    srclang = models.CharField(max_length=225, blank=True, null=True)
    sub_title_file = models.CharField(max_length=1000, null=True, blank=True)

    sub_title_lang2 = models.CharField(max_length=225, null=True, blank=True)
    srclang2 = models.CharField(max_length=225, blank=True, null=True)
    sub_title_file2 = models.CharField(max_length=1000, null=True, blank=True)

    duration = models.CharField(max_length=100)
    dou = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(f'{self.season_val}')

class series_comment(models.Model):
    pass

class episode_comment(models.Model):
    episode = models.ForeignKey(episode, related_name='series_comments', on_delete=models.CASCADE)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    series_name = models.ForeignKey(series, on_delete=models.CASCADE, null=True, blank=True)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.series_name)

class episode_review(models.Model):
    episode = models.ForeignKey(episode, related_name='series_reviews', on_delete=models.CASCADE)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    series_name = models.ForeignKey(series, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=5000)
    body = models.TextField()
    rate = models.IntegerField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.series_name)
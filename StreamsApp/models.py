from django.db import models
from django.contrib.auth.models import User
from movieapp.models import *
import uuid

class Stream(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    stream_id = models.CharField(max_length=225, default=uuid.uuid4())
    is_movie = models.BooleanField(default=False)
    is_series = models.BooleanField(default=False)
    movie = models.ForeignKey(movie, on_delete=models.CASCADE, blank=True, null=True)
    series = models.ForeignKey(series, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.is_movie:
            return str(self.movie)
        elif self.is_series:
            return str(self.series)
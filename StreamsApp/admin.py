from django.contrib import admin
from .models import *

class StreamAdmin(admin.ModelAdmin):

    list_display = ['creator', 'stream_id', 'is_movie', 'is_series', 'movie', 'series', 'date']

admin.site.register(Stream, StreamAdmin)
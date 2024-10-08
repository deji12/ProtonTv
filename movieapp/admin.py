from django.contrib import admin
from . import models
from import_export.admin import ImportExportModelAdmin

class MovieAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['name', 'category', 'duration', 'watch_hours', 'draft', 'new']
admin.site.register(models.movie, MovieAdmin)

class CommentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['movie', 'name', 'body', 'date']
admin.site.register(models.comment, CommentAdmin)

class ReviewAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['movie', 'name', 'title', 'rate', 'date']
admin.site.register(models.reviewss, ReviewAdmin)

class PhotoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['movie_name', 'series_name', 'pic']
admin.site.register(models.photos, PhotoAdmin)
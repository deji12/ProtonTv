from django.contrib import admin
from . import models
from import_export.admin import ImportExportModelAdmin

class SeriesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['name', 'rating', 'year', 'country', 'draft']

admin.site.register(models.series, SeriesAdmin)

class EpisodeCommentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['series_name','episode', 'name',  'body', 'date']

admin.site.register(models.episode_comment, EpisodeCommentAdmin)

class EpisodeReviewAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    list_display = ['series_name','episode', 'name', 'rate', 'body', 'date']
admin.site.register(models.episode_review, EpisodeReviewAdmin)

class SeasonAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['series_name','season_num', 'heading', 'collapse']

admin.site.register(models.season, SeasonAdmin)

class EpisodeAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['title', 'episode_num', 'series_name', 'season_val', 'duration', 'dou']

admin.site.register(models.episode, EpisodeAdmin)

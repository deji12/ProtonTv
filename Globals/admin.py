from django.contrib import admin
from . import models 
from import_export.admin import ImportExportModelAdmin
from .models import SiteInformation

class CategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['cat']

admin.site.register(models.Category, CategoryAdmin)

class RateAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['rate_value']
admin.site.register(models.rate, RateAdmin)

class YearAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['year_value']
admin.site.register(models.year, YearAdmin)

class SiteInformationAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('site_name', 'site_title', 'facebook_link', 'twitter_link', 'instagram_link', 'contact_email', 'contact_number')

admin.site.register(SiteInformation, SiteInformationAdmin)

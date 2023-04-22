from django.contrib import admin
from . import models 
from import_export.admin import ImportExportModelAdmin

class CategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['cat']

admin.site.register(models.Category, CategoryAdmin)

class RateAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['rate_value']
admin.site.register(models.rate, RateAdmin)

class YearAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['year_value']
admin.site.register(models.year, YearAdmin)

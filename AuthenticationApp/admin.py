from django.contrib import admin
from .models import Profile
from import_export.admin import ImportExportModelAdmin

class ProfileAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['user', 'verified', 'pricing_plan', 'email', 'comments', 'reviews', 'creation_date']

admin.site.register(Profile, ProfileAdmin)

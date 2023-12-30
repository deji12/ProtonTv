from django.db import models

class Category(models.Model):
    cat = models.CharField(max_length=1000)

    def __str__(self):
        return self.cat

class rate(models.Model):
    rate_value = models.CharField(max_length=1000)

class year(models.Model):
    year_value = models.CharField(max_length=200)

    def __str__(self):
        return self.year_value
    
from django.contrib.sites.models import Site

class SiteInformation(models.Model):
    site = models.OneToOneField(Site, on_delete=models.CASCADE)
    site_name = models.CharField(max_length=225, null=True, blank=True)
    site_title = models.CharField(max_length=225, null=True, blank=True)
    facebook_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)
    contact_email = models.EmailField(blank=True, null=True)
    contact_number = models.CharField(max_length=225, blank=True, null=True)
    footer_message = models.TextField(blank=True, null=True)
    contact_page_message = models.TextField(blank=True, null=True)
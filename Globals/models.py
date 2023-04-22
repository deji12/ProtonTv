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

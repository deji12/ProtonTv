# Generated by Django 4.2.1 on 2023-11-27 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Globals', '0001_initial'),
        ('SeriesApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='series',
            name='genre1',
        ),
        migrations.RemoveField(
            model_name='series',
            name='genre2',
        ),
        migrations.AddField(
            model_name='series',
            name='genre',
            field=models.ManyToManyField(blank=True, null=True, related_name='series_category', to='Globals.category'),
        ),
    ]

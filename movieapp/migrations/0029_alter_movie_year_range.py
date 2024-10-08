# Generated by Django 4.2.1 on 2023-12-30 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0028_alter_movie_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='year_range',
            field=models.CharField(blank=True, choices=[('', 'Select Year Range'), ('1950-1955', '1950-1955'), ('1955-1960', '1955-1960'), ('1960-1965', '1960-1965'), ('1965-1970', '1965-1970'), ('1970-1975', '1970-1975'), ('1975-1980', '1975-1980'), ('1980-1985', '1980-1985'), ('1985-1990', '1985-1990'), ('1990-1995', '1990-1995'), ('1995-2000', '1995-2000'), ('2000-2005', '2000-2005'), ('2005-2010', '2005-2010'), ('2010-2015', '2010-2015'), ('2015-2020', '2015-2020'), ('2020-2023', '2020-2023')], max_length=200, null=True),
        ),
    ]

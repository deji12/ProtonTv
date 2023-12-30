# Generated by Django 4.2.1 on 2023-12-11 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0025_alter_movie_age_alter_movie_country_alter_movie_year_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='duration',
            field=models.CharField(choices=[('10-20', '10-20'), ('20-30', '20-30'), ('30-40', '30-40'), ('40-50', '40-50'), ('50-60', '50-60'), ('60-70', '60-70'), ('70-80', '70-80'), ('80-90', '80-90'), ('90-100', '90-100'), ('100-110', '100-110'), ('110-120', '110-120'), ('120-130', '120-130'), ('130-140', '130-140'), ('140-150', '140-150'), ('150-160', '150-160'), ('160-170', '160-170'), ('170-180', '170-180'), ('180-190', '180-190'), ('190-200', '190-200'), ('200-210', '200-210'), ('210-220', '210-220'), ('220-230', '220-230'), ('230-240', '230-240'), ('240-250', '240-250'), ('250-260', '250-260'), ('260-270', '260-270'), ('270-280', '270-280'), ('280-290', '280-290'), ('290-300', '290-300'), ('300-310', '300-310')], max_length=100),
        ),
        migrations.AlterField(
            model_name='movie',
            name='year_range',
            field=models.CharField(blank=True, choices=[('1950-1955', '1950-1955'), ('1955-1960', '1955-1960'), ('1960-1965', '1960-1965'), ('1965-1970', '1965-1970'), ('1970-1975', '1970-1975'), ('1975-1980', '1975-1980'), ('1980-1985', '1980-1985'), ('1985-1990', '1985-1990'), ('1990-1995', '1990-1995'), ('1995-2000', '1995-2000'), ('2000-2005', '2000-2005'), ('2005-2010', '2005-2010'), ('2010-2015', '2010-2015'), ('2015-2020', '2015-2020'), ('2020-2023', '2020-2023')], max_length=200, null=True),
        ),
    ]

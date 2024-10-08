# Generated by Django 4.2.1 on 2023-12-11 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0026_alter_movie_duration_alter_movie_year_range'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='age',
            field=models.CharField(choices=[('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18')], default=13, max_length=20),
        ),
        migrations.AlterField(
            model_name='movie',
            name='duration',
            field=models.CharField(choices=[('20 minutes', '20 minutes'), ('30 minutes', '30 minutes'), ('40 minutes', '40 minutes'), ('50 minutes', '50 minutes'), ('60 minutes', '60 minutes'), ('70 minutes', '70 minutes'), ('80 minutes', '80 minutes'), ('90 minutes', '90 minutes'), ('100 minutes', '100 minutes'), ('110 minutes', '110 minutes'), ('120 minutes', '120 minutes'), ('130 minutes', '130 minutes'), ('140 minutes', '140 minutes'), ('150 minutes', '150 minutes'), ('160 minutes', '160 minutes'), ('170 minutes', '170 minutes'), ('180 minutes', '180 minutes'), ('190 minutes', '190 minutes'), ('200 minutes', '200 minutes'), ('210 minutes', '210 minutes'), ('220 minutes', '220 minutes'), ('230 minutes', '230 minutes'), ('240 minutes', '240 minutes'), ('250 minutes', '250 minutes'), ('260 minutes', '260 minutes'), ('270 minutes', '270 minutes'), ('280 minutes', '280 minutes'), ('290 minutes', '290 minutes'), ('300 minutes', '300 minutes'), ('310 minutes', '310 minutes')], max_length=100),
        ),
        migrations.AlterField(
            model_name='movie',
            name='year',
            field=models.CharField(choices=[('1990', '1990'), ('1991', '1991'), ('1992', '1992'), ('1993', '1993'), ('1994', '1994'), ('1995', '1995'), ('1996', '1996'), ('1997', '1997'), ('1998', '1998'), ('1999', '1999'), ('2000', '2000'), ('2001', '2001'), ('2002', '2002'), ('2003', '2003'), ('2004', '2004'), ('2005', '2005'), ('2006', '2006'), ('2007', '2007'), ('2008', '2008'), ('2009', '2009'), ('2010', '2010'), ('2011', '2011'), ('2012', '2012'), ('2013', '2013'), ('2014', '2014'), ('2015', '2015'), ('2016', '2016'), ('2017', '2017'), ('2018', '2018'), ('2019', '2019'), ('2020', '2020'), ('2021', '2021'), ('2022', '2022'), ('2023', '2023')], max_length=100),
        ),
    ]

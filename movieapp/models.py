from django.db import models
from django.contrib.auth.models import User
from SeriesApp.models import series
from Globals.models import *
import datetime

CATEGORY_CHOICE = [
    ("movie", "movie"),
    ("cartoon", "cartoon"),
]

AGE_CHOICE = [(f"{i}", f"{i}") for i in range(5, 19)]

current_year = datetime.datetime.now().year
YEAR_CHOICE = [(f"{year}", f"{year}") for year in range(1990, current_year + 3)]

YEAR_RANGES = [
    (f"{start}-{end}", f"{start}-{end}") for start, end in zip(range(1950, current_year + 1, 5), range(1955, (current_year + 4), 5))
]

# Adjust the last entry to cover the remaining years
# if current_year % 5 != 0:
#     last_range = (f"{current_year - (current_year % 5)}-{current_year}", f"{current_year - (current_year % 5)}-{current_year}")
#     YEAR_RANGES.append(last_range)

DURATION_RANGES = [
    (f"{start + 10} minutes", f"{start + 10} minutes") for start in range(10, 301, 10)
]

COUNTRY_CHOICES = [
    ('Afghanistan', 'Afghanistan'),
    ('Albania', 'Albania'),
    ('Algeria', 'Algeria'),
    ('Andorra', 'Andorra'),
    ('Angola', 'Angola'),
    ('Antigua and Barbuda', 'Antigua and Barbuda'),
    ('Argentina', 'Argentina'),
    ('Armenia', 'Armenia'),
    ('Australia', 'Australia'),
    ('Austria', 'Austria'),
    ('Azerbaijan', 'Azerbaijan'),
    ('Bahamas', 'Bahamas'),
    ('Bahrain', 'Bahrain'),
    ('Bangladesh', 'Bangladesh'),
    ('Barbados', 'Barbados'),
    ('Belarus', 'Belarus'),
    ('Belgium', 'Belgium'),
    ('Belize', 'Belize'),
    ('Benin', 'Benin'),
    ('Bhutan', 'Bhutan'),
    ('Bolivia', 'Bolivia'),
    ('Bosnia and Herzegovina', 'Bosnia and Herzegovina'),
    ('Botswana', 'Botswana'),
    ('Brazil', 'Brazil'),
    ('Brunei', 'Brunei'),
    ('Bulgaria', 'Bulgaria'),
    ('Burkina Faso', 'Burkina Faso'),
    ('Burundi', 'Burundi'),
    ('Cabo Verde', 'Cabo Verde'),
    ('Cambodia', 'Cambodia'),
    ('Cameroon', 'Cameroon'),
    ('Canada', 'Canada'),
    ('Central African Republic', 'Central African Republic'),
    ('Chad', 'Chad'),
    ('Chile', 'Chile'),
    ('China', 'China'),
    ('Colombia', 'Colombia'),
    ('Comoros', 'Comoros'),
    ('Congo (Congo-Brazzaville)', 'Congo (Congo-Brazzaville)'),
    ('Costa Rica', 'Costa Rica'),
    ('Croatia', 'Croatia'),
    ('Cuba', 'Cuba'),
    ('Cyprus', 'Cyprus'),
    ('Czechia (Czech Republic)', 'Czechia (Czech Republic)'),
    ('Denmark', 'Denmark'),
    ('Djibouti', 'Djibouti'),
    ('Dominica', 'Dominica'),
    ('Dominican Republic', 'Dominican Republic'),
    ('Ecuador', 'Ecuador'),
    ('Egypt', 'Egypt'),
    ('El Salvador', 'El Salvador'),
    ('Equatorial Guinea', 'Equatorial Guinea'),
    ('Eritrea', 'Eritrea'),
    ('Estonia', 'Estonia'),
    ('Eswatini (fmr. "Swaziland")', 'Eswatini (fmr. "Swaziland")'),
    ('Ethiopia', 'Ethiopia'),
    ('Fiji', 'Fiji'),
    ('Finland', 'Finland'),
    ('France', 'France'),
    ('Gabon', 'Gabon'),
    ('Gambia', 'Gambia'),
    ('Georgia', 'Georgia'),
    ('Germany', 'Germany'),
    ('Ghana', 'Ghana'),
    ('Greece', 'Greece'),
    ('Grenada', 'Grenada'),
    ('Guatemala', 'Guatemala'),
    ('Guinea', 'Guinea'),
    ('Guinea-Bissau', 'Guinea-Bissau'),
    ('Guyana', 'Guyana'),
    ('Haiti', 'Haiti'),
    ('Holy See', 'Holy See'),
    ('Honduras', 'Honduras'),
    ('Hungary', 'Hungary'),
    ('Iceland', 'Iceland'),
    ('India', 'India'),
    ('Indonesia', 'Indonesia'),
    ('Iran', 'Iran'),
    ('Iraq', 'Iraq'),
    ('Ireland', 'Ireland'),
    ('Israel', 'Israel'),
    ('Italy', 'Italy'),
    ('Jamaica', 'Jamaica'),
    ('Japan', 'Japan'),
    ('Jordan', 'Jordan'),
    ('Kazakhstan', 'Kazakhstan'),
    ('Kenya', 'Kenya'),
    ('Kiribati', 'Kiribati'),
    ('Kuwait', 'Kuwait'),
    ('Kyrgyzstan', 'Kyrgyzstan'),
    ('Laos', 'Laos'),
    ('Latvia', 'Latvia'),
    ('Lebanon', 'Lebanon'),
    ('Lesotho', 'Lesotho'),
    ('Liberia', 'Liberia'),
    ('Libya', 'Libya'),
    ('Liechtenstein', 'Liechtenstein'),
    ('Lithuania', 'Lithuania'),
    ('Luxembourg', 'Luxembourg'),
    ('Madagascar', 'Madagascar'),
    ('Malawi', 'Malawi'),
    ('Malaysia', 'Malaysia'),
    ('Maldives', 'Maldives'),
    ('Mali', 'Mali'),
    ('Malta', 'Malta'),
    ('Marshall Islands', 'Marshall Islands'),
    ('Mauritania', 'Mauritania'),
    ('Mauritius', 'Mauritius'),
    ('Mexico', 'Mexico'),
    ('Micronesia', 'Micronesia'),
    ('Moldova', 'Moldova'),
    ('Monaco', 'Monaco'),
    ('Mongolia', 'Mongolia'),
    ('Montenegro', 'Montenegro'),
    ('Morocco', 'Morocco'),
    ('Mozambique', 'Mozambique'),
    ('Myanmar (formerly Burma)', 'Myanmar (formerly Burma)'),
    ('Namibia', 'Namibia'),
    ('Nauru', 'Nauru'),
    ('Nepal', 'Nepal'),
    ('Netherlands', 'Netherlands'),
    ('New Zealand', 'New Zealand'),
    ('Nicaragua', 'Nicaragua'),
    ('Niger', 'Niger'),
    ('Nigeria', 'Nigeria'),
    ('North Korea', 'North Korea'),
    ('North Macedonia', 'North Macedonia'),
    ('Norway', 'Norway'),
    ('Oman', 'Oman'),
    ('Pakistan', 'Pakistan'),
    ('Palau', 'Palau'),
    ('Palestine State', 'Palestine State'),
    ('Panama', 'Panama'),
    ('Papua New Guinea', 'Papua New Guinea'),
    ('Paraguay', 'Paraguay'),
    ('Peru', 'Peru'),
    ('Philippines', 'Philippines'),
    ('Poland', 'Poland'),
    ('Portugal', 'Portugal'),
    ('Qatar', 'Qatar'),
    ('Romania', 'Romania'),
    ('Russia', 'Russia'),
    ('Rwanda', 'Rwanda'),
    ('Saint Kitts and Nevis', 'Saint Kitts and Nevis'),
    ('Saint Lucia', 'Saint Lucia'),
    ('Saint Vincent and the Grenadines', 'Saint Vincent and the Grenadines'),
    ('Samoa', 'Samoa'),
    ('San Marino', 'San Marino'),
        ('Sao Tome and Principe', 'Sao Tome and Principe'),
    ('Saudi Arabia', 'Saudi Arabia'),
    ('Senegal', 'Senegal'),
    ('Serbia', 'Serbia'),
    ('Seychelles', 'Seychelles'),
    ('Sierra Leone', 'Sierra Leone'),
    ('Singapore', 'Singapore'),
    ('Slovakia', 'Slovakia'),
    ('Slovenia', 'Slovenia'),
    ('Solomon Islands', 'Solomon Islands'),
    ('Somalia', 'Somalia'),
    ('South Africa', 'South Africa'),
    ('South Korea', 'South Korea'),
    ('South Sudan', 'South Sudan'),
    ('Spain', 'Spain'),
    ('Sri Lanka', 'Sri Lanka'),
    ('Sudan', 'Sudan'),
    ('Suriname', 'Suriname'),
    ('Sweden', 'Sweden'),
    ('Switzerland', 'Switzerland'),
    ('Syria', 'Syria'),
    ('Tajikistan', 'Tajikistan'),
    ('Tanzania', 'Tanzania'),
    ('Thailand', 'Thailand'),
    ('Timor-Leste', 'Timor-Leste'),
    ('Togo', 'Togo'),
    ('Tonga', 'Tonga'),
    ('Trinidad and Tobago', 'Trinidad and Tobago'),
    ('Tunisia', 'Tunisia'),
    ('Turkey', 'Turkey'),
    ('Turkmenistan', 'Turkmenistan'),
    ('Tuvalu', 'Tuvalu'),
    ('Uganda', 'Uganda'),
    ('Ukraine', 'Ukraine'),
    ('United Arab Emirates', 'United Arab Emirates'),
    ('United Kingdom', 'United Kingdom'),
    ('United States of America', 'United States of America'),
    ('Uruguay', 'Uruguay'),
    ('Uzbekistan', 'Uzbekistan'),
    ('Vanuatu', 'Vanuatu'),
    ('Vatican City', 'Vatican City'),
    ('Venezuela', 'Venezuela'),
    ('Vietnam', 'Vietnam'),
    ('Yemen', 'Yemen'),
    ('Zambia', 'Zambia'),
    ('Zimbabwe', 'Zimbabwe'),
]

class movie(models.Model):
    name = models.CharField(max_length=20000)
    info = models.TextField()
    video = models.CharField(max_length=10000, null=True, blank=True)

    sub_title_language = models.CharField(max_length=225, null=True, blank=True)
    srclanguage = models.CharField(max_length=225, blank=True, null=True)
    sub_title_file = models.CharField(max_length=1000, null=True, blank=True)

    sub_title_language2 = models.CharField(max_length=225, null=True, blank=True)
    srclanguage2 = models.CharField(max_length=225, blank=True, null=True)
    sub_title_file2 = models.CharField(max_length=1000, null=True, blank=True)

    thumbnail = models.FileField(upload_to='thumb/')
    age = models.CharField(default=13, max_length=20, choices=AGE_CHOICE)
    category = models.CharField(choices=CATEGORY_CHOICE, max_length=200)
    genre = models.ManyToManyField(Category, related_name='category', null=True, blank=True)
    rating = models.CharField(max_length=100)
    year = models.CharField(max_length=100, choices=YEAR_CHOICE)
    year_range = models.CharField(max_length=200, null=True, blank=True, choices=[("", "Select Year Range")] + YEAR_RANGES)
    duration = models.CharField(max_length=100, choices=DURATION_RANGES)
    country = models.CharField(max_length=200, choices=COUNTRY_CHOICES)
    date_added = models.DateField(auto_now_add=True, null=True, blank=True)
    clicks = models.IntegerField(null=True, blank=True, default=0)
    watch_hours = models.FloatField(default=0.0)
    new = models.BooleanField(default=False)
    draft = models.BooleanField(default=False)
    premier = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    def return_movie_comments(self):

        return comment.objects.filter(movie=self).order_by('-date')
    
    def return_movie_reviews(self):

        return reviewss.objects.filter(movie=self).order_by('-date')
    
    def return_movie_pictures(self):

        return photos.objects.filter(movie_name=self)

class comment(models.Model):
    movie = models.ForeignKey(movie, related_name='movie_comment', on_delete=models.CASCADE)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.movie)

class reviewss(models.Model):
    movie = models.ForeignKey(movie, related_name='movie_review', on_delete=models.CASCADE)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=5000)
    body = models.TextField()
    rate = models.IntegerField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.movie)

class photos(models.Model):
    series_name = models.ForeignKey(series, on_delete=models.CASCADE, null=True, blank=True)
    movie_name = models.ForeignKey(movie, on_delete=models.CASCADE, null=True, blank=True)
    pic = models.FileField(upload_to='movie-photos')

    def __str__(self):
        return str(self.movie_name)
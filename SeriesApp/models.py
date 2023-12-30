from django.db import models
from Globals.models import *
from django.contrib.auth.models import User
import datetime

CATEGORY_CHOICE = [
    ("series", "series"),
    ("anime", "anime"),
]

AGE_CHOICE = [(f"{i}", f"{i}") for i in range(5, 19)]

current_year = datetime.datetime.now().year
YEAR_CHOICE = [(f"{year}", f"{year}") for year in range(1990, current_year + 1)]

YEAR_RANGES = [
    (f"{start}-{end}", f"{start}-{end}") for start, end in zip(range(1950, current_year, 5), range(1955, current_year + 1, 5))
]

# Adjust the last entry to cover the remaining years
if current_year % 5 != 0:
    last_range = (f"{current_year - (current_year % 5)}-{current_year}", f"{current_year - (current_year % 5)}-{current_year}")
    YEAR_RANGES.append(last_range)

DURATION_RANGES = [
    (f"{start + 10} minutes", f"{start + 10} minutes") for start in range(10, 301, 10)
]

SEASON_NUMBER = [(f"{i}", f"{i}") for i in range(1, 11)]
HEADING = [
    ("headingOne", "headingOne"),
    ("headingTwo", "headingTwo"),
    ("headingThree", "headingThree"),
    ("headingFour", "headingFour"),
    ("headingFive", "headingFive"),
    ("headingSix", "headingSix"),
    ("headingSeven", "headingSeven"),
    ("headingEight", "headingEight"),
    ("headingNine", "headingNine"),
    ("headingTen", "headingTen"),
]
COLLAPSE = [
    ("collapseOne", "collapseOne"),
    ("collapseTwo", "collapseTwo"),
    ("collapseThree", "collapseThree"),
    ("collapseFour", "collapseFour"),
    ("collapseFive", "collapseFive"),
    ("collapseSix", "collapseSix"),
    ("collapseSeven", "collapseSeven"),
    ("collapseEight", "collapseEight"),
    ("collapseNine", "collapseNine"),
    ("collapseTen", "collapseTen"),
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

class series(models.Model):
    name = models.CharField(max_length=20000)
    info = models.TextField()
    thumbnail = models.FileField(upload_to='thumb/series/')
    age = models.CharField(default=13, max_length=20, choices=AGE_CHOICE)
    genre = models.ManyToManyField(Category, related_name='series_category', null=True, blank=True)
    rating = models.CharField(max_length=100)
    series_air_date = models.DateField(auto_now_add=True)
    year_range = models.CharField(max_length=200, null=True, blank=True, choices=YEAR_RANGES)
    year = models.CharField(max_length=100, choices=YEAR_CHOICE)
    country = models.CharField(max_length=200, choices=COUNTRY_CHOICES)
    clicks = models.IntegerField(null=True, blank=True, default=0)
    category = models.CharField(max_length=200, choices=CATEGORY_CHOICE)
    watch_hours = models.FloatField(default=0.0)
    is_series_new = models.BooleanField(default=False)
    premier = models.BooleanField(default=False)
    draft = models.BooleanField(default=False)

    def __str__(self):
        return str(self.name)
    
    def get_series_images(self):
        from movieapp.models import photos
        return photos.objects.filter(series_name=self)
    
class season(models.Model):
    series_name = models.ForeignKey(series, related_name='season_val', on_delete=models.CASCADE)
    season_num = models.CharField(max_length=100, choices=SEASON_NUMBER)
    heading = models.CharField(max_length=100, blank=True, null=True, choices=HEADING)
    collapse = models.CharField(max_length=100, blank=True, null=True, choices=COLLAPSE)
    

    def __str__(self):
        return str(f'{self.series_name} | Season {self.season_num}')

class episode(models.Model):
    title = models.CharField(max_length=200, default='title')
    series_name = models.ForeignKey(series, related_name='season_epi', on_delete=models.CASCADE)
    season_val = models.ForeignKey(season, related_name='episode', on_delete=models.CASCADE)   
    episode_num = models.IntegerField( default=1) 
    video = models.CharField(max_length=10000, null=True, blank=True)

    sub_title_lang = models.CharField(max_length=225, null=True, blank=True)
    srclang = models.CharField(max_length=225, blank=True, null=True)
    sub_title_file = models.CharField(max_length=1000, null=True, blank=True)

    sub_title_lang2 = models.CharField(max_length=225, null=True, blank=True)
    srclang2 = models.CharField(max_length=225, blank=True, null=True)
    sub_title_file2 = models.CharField(max_length=1000, null=True, blank=True)

    duration = models.CharField(max_length=100, choices=DURATION_RANGES)
    date_of_upload = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(f'{self.season_val}')

class series_comment(models.Model):
    pass

class episode_comment(models.Model):
    episode = models.ForeignKey(episode, related_name='series_comments', on_delete=models.CASCADE)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    series_name = models.ForeignKey(series, on_delete=models.CASCADE, null=True, blank=True)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.series_name)

class episode_review(models.Model):
    episode = models.ForeignKey(episode, related_name='series_reviews', on_delete=models.CASCADE)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    series_name = models.ForeignKey(series, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=5000)
    body = models.TextField()
    rate = models.IntegerField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.series_name)
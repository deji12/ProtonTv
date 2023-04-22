from django.urls import path
from . import views

urlpatterns = [
    path('series/detail/<str:name>/', views.series_detail, name='series-detail'),
    path('series/detail/<str:name>/<str:seasons>/<str:epi>/', views.series_detail_epi, name='series-detail-epi'),
    path('series/', views.Series, name='series'),
    path('anime/', views.Anime, name='anime'),
]
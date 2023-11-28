from django.urls import path
from . import views

urlpatterns = [
    path('movies/grid-catalog/', views.catalog_grid, name='cat1'),
    path('movies/list-catalog/', views.catalog_list, name='cat2'),
]
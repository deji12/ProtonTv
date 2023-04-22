from django.urls import path
from . import views

urlpatterns = [
    path('catalog-1/', views.catalog_grid, name='cat1'),
    path('catalog-2/', views.catalog_list, name='cat2'),
]
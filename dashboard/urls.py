from django.urls import path
from dashboard import views

urlpatterns = [
    path('dashboard/home/', views.DashboardHome, name='d-home'),
    path('dashboard/add-new-item/', views.AddNewItem, name='add-item'),
    path('dashboard/movie-catalog/', views.MovieCatalog, name='catalog'),
    path('dashboard/series-catalog/', views.SeriesCatalog, name='series-catalog'),
    path('dashboard/not-found/', views.NotFound, name='not-found'),
    path('dashboard/series-catalog/user/draft-post/series/<str:name>/', views.DraftPostSeries, name='draft-post-series'),
    path('dashboard/movie-catalog/user/draft-post/movies/<str:name>/', views.DraftPostMovies, name='draft-post-movies'),
    path('dashboard/users/change-user-password/<str:email>/', views.ChangePassword, name='change-user-password'),
    path('dashboard/catalog/search/', views.search, name='search-catalog'),
    path('dashboard/catalog/filter-by-date-created/', views.Date_Created, name='filter-created'),
    path('dashboard/catalog/filter-by-user-date-creation/', views.DateUserCreated, name='filter-date-created'),
]
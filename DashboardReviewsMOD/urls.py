from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/reviews/delete-movie-review/<str:name>/<str:movie_name>/<str:body>/', views.DeleteReviewMovies, name='delete-review-movie'),
    path('dashboard/reviews/delete-series-review/<str:name>/<str:title>/<str:series_name>/<str:comment_content>/', views.DeleteReviewSeries, name='delete-review-series'),
    path('dashboard/reviews/', views.Reviews, name='reviews'),
    path('dashboard/comments/filter-user-reviews/', views.FilterReviews, name='filter-comment-reviews'),

]
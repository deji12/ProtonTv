from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/comments/', views.Comments, name='comments'),
    path('dashboard/comments/delete/<str:name>/<str:title>/<str:series_name>/<str:comment_content>/', views.DeleteCommentSeries, name='delete-comment-series'),
    path('dashboard/comments/delete-movie/<str:name>/<str:movie_name>/<str:body>/', views.DeleteCommentMovies, name='delete-comment-movie'),
    path('dashboard/edit-user/<str:email>/comments/delete/<str:name>/<str:title>/<str:series_name>/<str:comment_content>/', views.DeleteCommentSeries, name='edit-user2'),
    path('dashboard/comments/filter-user-comments/', views.FilterCommentsSeries, name='filter-comment-series'),

]
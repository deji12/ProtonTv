from django.urls import path
from . import views

urlpatterns = [
    path('detail-view/<str:name>/', views.detail, name='detail'),
    path('watch-party/<str:name>/<str:stream_id>', views.MovieStreamDetail, name='watch-party'),
]
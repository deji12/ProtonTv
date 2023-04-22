from django.urls import path
from . import views

urlpatterns = [
    path('detail-view/<str:name>/', views.detail, name='detail'),
]
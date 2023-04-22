from django.urls import path
from . import views 

urlpatterns = [
    path('login/', views.signin, name='login'),
    path('register/', views.signup, name='register'),
    path('logout/', views.LogoutView, name='logout'),
    path('forgot-password/', views.forgot_password, name='fp'),
    path('auth/reset-password/', views.reset_password, name='reset-password'),
    path('auth/reset-password/<str:name>/', views.PasswordResedtView, name='reset_view'),
    path('auth/password-reset-sent/', views.password_reset_sent, name='reset-sent'),
    path('profile/', views.profile, name='profile'),
]
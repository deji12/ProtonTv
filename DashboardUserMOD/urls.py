from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/edit-user/<str:email>/', views.EditUser, name='edit-user'),
    path('dashboard/users/', views.AllUsers, name='users'),
    path('dashboard/users/user/ban-user/<str:email>/', views.BanUser, name='ban-user'),
    path('dashboard/users/edit-user-profile/<str:email>/', views.EditProfileDetails, name='edit-user-profile'),
    path('dashbboard/users/filter-verified-users/', views.VerifiedUsers, name='verified-users'),
    path('dashbboard/users/filter-banned-users/', views.BannedUsers, name='banned-users'),
]
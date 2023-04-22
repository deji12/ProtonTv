from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('movieapp.urls')),
    path('', include('dashboard.urls')),
    path('api/', include('protontvapi.urls')),
    path('', include('SearchApp.urls')),
    path('', include('AuthenticationApp.urls')),
    path('', include('CatalogApp.urls')),
    path('', include('SeriesApp.urls')),
    path('', include('MoviePlayerApp.urls')),
    path('', include('DashboardCommentMOD.urls')),
    path('', include('DashboardReviewsMOD.urls')),
    path('', include('DashboardUserMOD.urls')),
]

handler404 = handler404 = 'movieapp.views.NotFound'

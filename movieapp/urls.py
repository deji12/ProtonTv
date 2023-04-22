from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('pricing-plan/', views.pricing, name='pricing'),
    path('frequently-asked-questions/', views.faq, name='faq'),
    path('about-us/', views.about, name='about'),
    path('privacy/', views.privacy, name='privacy'),
    path('contact-us/', views.contacts, name='contact'),
    path('404/', views.NotFound, name='404'),
]


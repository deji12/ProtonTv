from django.urls import path
from .consumers import PartyConsumer

websocket_urlpatterns = [
    path('ws/watch-party/<str:stream_id>/', PartyConsumer.as_asgi())
]
"""
ASGI config for movie project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movie.settings')
from channels.routing import ProtocolTypeRouter, URLRouter
from StreamsApp import routing

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    # "websocket": URLRouter(
    #     websocket_urlpatterns
    # )
    "http": django_asgi_app,
    "websocket": URLRouter(
            routing.websocket_urlpatterns
        )
    
}) 
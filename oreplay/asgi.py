"""
ASGI config for oreplay project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import apps.websocket.routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "oreplay.settings")

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),  # Maneja las solicitudes HTTP
        "websocket": AuthMiddlewareStack(
            URLRouter(
                apps.websocket.routing.websocket_urlpatterns  # Define las rutas WebSocket en tu aplicación
            )
        ),
    }
)

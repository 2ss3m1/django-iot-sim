import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
import sensors.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'agrisol_dashboard.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            sensors.routing.websocket_urlpatterns
        )
    ),
})

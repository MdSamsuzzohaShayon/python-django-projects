# https://channels.readthedocs.io/en/stable/topics/routing.html
from channels.auth import AuthMiddlewareStack
import chat.routing

# Users have to login to use chat room
from channels.routing import ProtocolTypeRouter, URLRouter

application = ProtocolTypeRouter({
    "websocker": AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    )
})

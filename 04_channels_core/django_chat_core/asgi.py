"""
ASGI config for django_chat_core project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from home.consumers import *

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_chat_core.settings")

application = get_asgi_application()

# While consumers are valid ASGI applications, you don’t want to just write one and have that be the only thing you can give to protocol servers like Daphne. Channels provides routing classes that allow you to combine and stack your consumers (and any other valid ASGI application) to dispatch based on what the connection is.
wp_patters = [
    path('ws/test/', TestConsumer.as_asgi()),
    path('ws/new/', NewConsumer.as_asgi()),
]

application = ProtocolTypeRouter({
    'websocket': URLRouter(wp_patters)
})

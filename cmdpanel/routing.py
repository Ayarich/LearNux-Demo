# cmdpanel/routing.py
from django.urls import path
from serverconsole import consumers

websocket_urlpatterns = [
    path("ws/terminal/", consumers.TerminalConsumer.as_asgi()),
]

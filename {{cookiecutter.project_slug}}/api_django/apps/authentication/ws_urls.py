from apps.authentication.views.ws_echo import Echo
from django.urls import path

websocket_urlpatterns = [
    path('echo/', Echo.as_asgi()),
]

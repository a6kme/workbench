from apps.authentication import ws_urls
from channels.routing import URLRouter
from django.urls import path

websocket_urlpatterns = [
    path('ws/auth/', URLRouter(ws_urls.websocket_urlpatterns)),
]

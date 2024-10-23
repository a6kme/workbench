"""
ASGI config for api project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import importlib
import json
import os

from channels.auth import AuthMiddlewareStack
from channels.db import database_sync_to_async
from channels.exceptions import DenyConnection
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from rest_framework.exceptions import AuthenticationFailed

from api.ws_urls import websocket_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings')


class WebSocketAuthenticationMiddleware:
    """
    Custom middleware to authenticate WebSocket users using the SupabaseAuthentication class
    """

    def __init__(self, inner):
        self.inner = inner

    async def __call__(self, scope, receive, send):
        # Authenticate the user
        try:
            scope['user'] = await self.authenticate_user(scope)
        except AuthenticationFailed as e:
            # Send a 403-like error message to the WebSocket client and close the connection
            await self.close_connection(send, json.dumps({
                'message': str(e)
            }))
            return

        # Call the next middleware or consumer
        try:
            return await self.inner(scope, receive, send)
        except ValueError as e:
            await self.close_connection(send, json.dumps({
                'message': str(e)
            }))
            return

    @database_sync_to_async
    def authenticate_user(self, scope):
        """
        Authenticate the user using the SupabaseAuthentication class
        """
        auth_models = importlib.import_module('django.contrib.auth.models')

        # Get the token from query parameters or headers
        token = scope['query_string'].decode().split('token=')[-1]

        if not token:
            raise AuthenticationFailed('token not provided')

        # Use the DRF SupabaseAuthentication class
        auth_supabase = importlib.import_module('api.auth_supabase')

        supabase_auth = auth_supabase.SupabaseAuthentication()

        # Mock the DRF request object with headers and token
        class DummyRequest:
            headers = {'Authorization': f'Bearer {token}'}

        user, _ = supabase_auth.authenticate(DummyRequest())
        return user

    async def close_connection(self, send, error_message):
        """
        Send a 403 error message over the WebSocket and close the connection.
        """
        # Accept the WebSocket connection
        await send({
            "type": "websocket.accept"
        })

        # Send error message to the client
        await send({
            "type": "websocket.send",
            "text": error_message,
        })
        # Close the WebSocket connection with a custom close code
        await send({
            "type": "websocket.close",
            "code": 4037  # Custom close code representing a 403 Forbidden
        })


application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": WebSocketAuthenticationMiddleware(AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        ))
    ),
})

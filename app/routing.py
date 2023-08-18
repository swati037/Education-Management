from django.urls import re_path
from . import consumers
websocket_urlpatterns = [
    re_path(r'meeting',consumers.ChatConsumer.as_asgi()),
]
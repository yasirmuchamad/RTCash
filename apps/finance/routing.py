
from django.urls import re_path
from .consumers import BalanceConsumer

websocket_urlpatterns = [
    re_path(r'ws/balance/$', BalanceConsumer.as_asgi()),
]

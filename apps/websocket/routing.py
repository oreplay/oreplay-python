from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(
        r"ws/category/(?P<category>\w+)/stage/(?P<stage>\w+)/$",
        consumers.CategoryStageConsumer.as_asgi(),
    ),
]

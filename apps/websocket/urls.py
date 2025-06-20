from django.urls import path
from .views import NotifyUpdateView

urlpatterns = [
    path("notify-update/", NotifyUpdateView.as_view(), name="notify_update"),
]

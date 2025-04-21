from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import OrganizerViewSet

# Configuración del enrutador
router = DefaultRouter()
router.register(r"organizers", OrganizerViewSet)

urlpatterns = [
    path("", include(router.urls)),  # Registra las rutas del enrutador
]

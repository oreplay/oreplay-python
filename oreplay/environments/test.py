from .base import *  # Importa la configuración base

# Activar modo de depuración
DEBUG = True

# Base de datos en memoria para pruebas
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",  # Base de datos en memoria
    }
}

# Cache basado en memoria para pruebas
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "unique-test-cache",
    }
}

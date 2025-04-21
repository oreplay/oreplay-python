from functools import wraps

from django.http import JsonResponse
from django.utils.timezone import now

from apps.users.models import AccessToken, User


class TokenExpired(Exception):
    """Excepción para indicar que el token ha expirado."""

    pass


def token_required(func):
    @wraps(func)
    def wrapper(view, request, *args, **kwargs):
        token = request.headers.get("Authorization")
        if not token:
            return JsonResponse({"error": "Token missing"}, status=401)

        try:
            token = token.split(" ")[1]
            access_token = AccessToken.objects.get(access_token=token)

            if access_token.expires < now():
                raise TokenExpired("The token has expired.")
        except AccessToken.DoesNotExist:
            return JsonResponse({"error": "Invalid token"}, status=401)
        except TokenExpired as e:
            return JsonResponse({"error": str(e)}, status=401)

        # Si el token es válido, proceder
        return func(view, request, *args, **kwargs)

    return wrapper

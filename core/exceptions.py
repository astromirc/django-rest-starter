from rest_framework import status
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    # Customización del mensaje de error 429 (Too Many Requests)
    if response and response.status_code == status.HTTP_429_TOO_MANY_REQUESTS:
        response.data["detail"] = "Has alcanzado el límite de solicitudes permitidas."

        wait = getattr(exc, "wait", None)
        if wait is not None:
            response.data["wait"] = wait

    return response

from rest_framework import status
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):

    response = exception_handler(exc, context)

    if response is None:
        return None

    if response.status_code == status.HTTP_400_BAD_REQUEST:
        message = "Validation failed."

    elif response.status_code == status.HTTP_401_UNAUTHORIZED:
        message = "Authentication failed."

    elif response.status_code == status.HTTP_403_FORBIDDEN:
        message = "Permission denied."

    elif response.status_code == status.HTTP_404_NOT_FOUND:
        message = "Resource not found."

    else:
        message = "Request failed."

    response.data = {
        "success": False,
        "message": message,
        "errors": response.data,
    }

    return response
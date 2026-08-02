from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):

    response = exception_handler(
        exc,
        context,
    )

    if response is None:
        return None

    message = response.data.get(
        "detail",
        "Something went wrong."
    )

    response.data = {
        "success": False,
        "message": message,
    }

    return response
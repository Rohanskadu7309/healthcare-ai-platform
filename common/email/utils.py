from django.conf import settings


def build_frontend_url(path: str) -> str:
    """
    Build frontend URL.
    """

    return f"{settings.FRONTEND_URL.rstrip('/')}/{path.lstrip('/')}"
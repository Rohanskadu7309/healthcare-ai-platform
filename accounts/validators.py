import re

from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers

User = get_user_model()

class RegistrationValidator:

    @staticmethod
    def validate_password(password: str):

        if len(password) < 8:
            raise serializers.ValidationError(
                "Password must contain at least 8 characters."
            )

        if not re.search(r"[A-Z]", password):
            raise serializers.ValidationError(
                "Password must contain one uppercase letter."
            )

        if not re.search(r"[a-z]", password):
            raise serializers.ValidationError(
                "Password must contain one lowercase letter."
            )

        if not re.search(r"\d", password):
            raise serializers.ValidationError(
                "Password must contain one number."
            )

        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            raise serializers.ValidationError(
                "Password must contain one special character."
            )

        return password
    

def validate_user_email(email):
    """
    Validate email format and uniqueness.
    """
    try:
        validate_email(email)
    except Exception:
        raise ValidationError("Enter a valid email address.")

    if User.objects.filter(email__iexact=email).exists():
        raise ValidationError("A user with this email already exists.")
    

def validate_user_password(password):
    """
    Validate password using Django's built-in validators.
    """
    try:
        validate_password(password)
    except Exception as e:
        raise ValidationError(e.messages)
    

def validate_confirm_password(password, confirm_password):
    """
    Ensure password and confirm password match.
    """
    if password != confirm_password:
        raise ValidationError("Passwords do not match.")
    

def validate_existing_active_user_email(email):
    """
    Validate that an active user exists with the given email.
    """
    user = User.objects.filter(email__iexact=email, is_active=True,).first()

    if not user:
        raise ValidationError(
            "No active account found with this email."
        )

    return user
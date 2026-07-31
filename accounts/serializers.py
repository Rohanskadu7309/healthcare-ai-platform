from rest_framework import serializers

from .models import User
from .validators import RegistrationValidator, validate_user_email, validate_user_password, validate_confirm_password

class RegisterSerializer(serializers.Serializer):

    first_name = serializers.CharField(required=False, allow_blank=True, max_length=100,)
    last_name = serializers.CharField(required=False, allow_blank=True, max_length=100,)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, min_length=8,)
    confirm_password = serializers.CharField(write_only=True, min_length=8,)

    def validate_email(self, value):
        validate_user_email(value)
        return value.lower()

    def validate_password(self, value):
        validate_user_password(value)
        return value

    def validate(self, attrs):
        validate_confirm_password(
            attrs["password"],
            attrs["confirm_password"],
        )
        return attrs
    

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    
    def validate_email(self, value):
        return value.lower()
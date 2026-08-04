from django.conf import settings
from django.db import transaction
from django.contrib.auth import get_user_model, authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError, AuthenticationFailed
from rest_framework.exceptions import ValidationError

from common.email.services import EmailService
from .models import PasswordResetRequest

User = get_user_model()


class RegistrationService:

    @staticmethod
    def register(validated_data):

        validated_data.pop("confirm_password")

        password = validated_data.pop("password")

        user = User.objects.create_user(
            password=password,
            **validated_data,
        )

        return user
    

class LoginService:
    
    @staticmethod
    def login(validated_data):
        
        email = validated_data['email']
        password = validated_data['password']
        
        user = authenticate(
            email = email,
            password = password,
        )
        
        if user is None:
            raise AuthenticationFailed("Invalid email or password.")
            
        refresh = RefreshToken.for_user(user)

        return {
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "user": user,
        }
        

class RefreshTokenService:
    
    @staticmethod
    def refresh(validated_data):
        
        try:
            refresh = RefreshToken(validated_data["refresh"])
            access = str(refresh.access_token)
            
            return {
                "access": access
            }
            
        except TokenError:
            
            raise AuthenticationFailed("Invalid or expired refresh token.")
        

class LogoutService:
    
    @staticmethod
    def logout(validated_data):
        
        try:
            token = RefreshToken(validated_data["refresh"])
            
            token.blacklist()
            
        except TokenError:
            
            raise AuthenticationFailed("Invalid or expired refresh token.")
        

class ProfileService:

    @staticmethod
    def get_profile(user):
        
        return user
    
    @staticmethod
    def update_profile(user, validated_data):
        
        user.first_name = validated_data.get("first_name", user.first_name)
        user.last_name = validated_data.get("last_name", user.last_name)
        
        user.save(update_fields=["first_name", "last_name"])
        
        return user
    

class ChangePasswordService:

    @staticmethod
    def change_password(user, validated_data):
        
        old_password = validated_data["old_password"]
        new_password = validated_data["new_password"]
        
        if not user.check_password(old_password):
            raise AuthenticationFailed("Old password is incorrect.")
        
        if old_password == new_password:
            raise ValidationError("New password cannot be the same as the old password.")
        
        user.set_password(new_password)
        user.save(update_fields=["password"])
        
        return user
    

class ForgotPasswordService:
    
    @staticmethod
    def send_reset_email(validated_data):
        
        pass
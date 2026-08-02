from django.contrib.auth import get_user_model, authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError, AuthenticationFailed

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
            
            raise ValueError("Invalid or expired refresh token.")
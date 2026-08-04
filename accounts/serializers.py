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
    

class RefreshTokenSerializer(serializers.Serializer):
    
    refresh = serializers.CharField()
    

class LogoutSerializer(serializers.Serializer):
    
    refresh = serializers.CharField()
    

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = User
        fields = ["id", "email", "first_name", "last_name"]
        read_only_fields = fields
        
        
class UpdateProfileSerializer(serializers.ModelSerializer):
    
    first_name = serializers.CharField(required=False, allow_blank=True, max_length=100,)
    last_name = serializers.CharField(required=False, allow_blank=True, max_length=100,)

    class Meta:
        
        model = User
        fields = ["first_name", "last_name"]
        
    def validate_first_name(self, value):
        
        return value.strip()
    
    def validate_last_name(self, value):
        
        return value.strip()
    

class ChangePasswordSerializer(serializers.Serializer):
    
    old_password = serializers.CharField(write_only=True, min_length=8)
    new_password = serializers.CharField(write_only=True, min_length=8)
    confirm_new_password = serializers.CharField(write_only=True, min_length=8)

    def validate_new_password(self, value):
        validate_user_password(value)
        
        return value

    def validate(self, attrs):
        validate_confirm_password(
            attrs["new_password"],
            attrs["confirm_new_password"],
        )
        
        return attrs
    

class ForgotPasswordSerializer(serializers.Serializer):
    
    email = serializers.EmailField()

    def validate_email(self, value):
        
        email = value.strip().lower()
    
        if not User.objects.filter(email__iexact=email, is_active=True).exists():
            
            raise serializers.ValidationError("If an account exists with this email, a password reset link has been sent.")
        
        return email
    

class ResetPasswordSerializer(serializers.Serializer):

    token = serializers.CharField()
    new_password = serializers.CharField(write_only=True, min_length=8)
    confirm_new_password = serializers.CharField(write_only=True, min_length=8)

    def validate_new_password(self, value):
        validate_user_password(value)
        
        return value

    def validate(self, attrs):
        validate_confirm_password(
            attrs["new_password"],
            attrs["confirm_new_password"],
        )

        return attrs
import secrets

from datetime import timedelta
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager



class User(AbstractBaseUser, PermissionsMixin):
    
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_email_verified = models.BooleanField(default=False)
    role = models.ForeignKey("authorization.Role", on_delete=models.SET_NULL, null=True, blank=True, related_name="users")
    date_joined = models.DateTimeField(auto_now_add=True)
    objects = UserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        
        db_table = "users"

    def __str__(self):
        
        return self.email
    

class PasswordResetRequest(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="password_reset_requests")
    token = models.CharField(max_length=128, unique=True, editable=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    
    class Meta:
        
        ordering = ["-created_at"]
        
        indexes = [
            models.Index(fields=["user", "is_active"]),
        ]
        
        verbose_name = "Password Reset Request"
        verbose_name_plural = "Password Reset Requests"
        
    def save(self, *args, **kwargs):
        
        if not self.token:
            self.token = secrets.token_urlsafe(48)
            
        if not self.expires_at:
            self.expires_at = timezone.now() + timedelta(hours=1)
            
        super().save(*args, **kwargs)
    
    @property    
    def is_expired(self):
        
        return timezone.now() > self.expires_at
    
    def __str__(self):
        
        return f"{self.user.email}"
    

class EmailVerification(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="email_verifications")
    token = models.CharField(max_length=128, unique=True, editable=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    
    class Meta:
        
        ordering = ["-created_at"]
        
        indexes = [
            models.Index(fields=["user", "token", "is_active"]),
        ]
        
        verbose_name = "Email Verification"
        verbose_name_plural = "Email Verifications"
        
    def save(self, *args, **kwargs):
        
        if not self.token:
            self.token = secrets.token_urlsafe(48)
            
        if not self.expires_at:
            self.expires_at = timezone.now() + timedelta(hours=24)
            
        super().save(*args, **kwargs)
    
    @property    
    def is_expired(self):
        
        return timezone.now() > self.expires_at
    
    def __str__(self):
        
        return self.user.email
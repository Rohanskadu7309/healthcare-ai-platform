from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, PasswordResetRequest, EmailVerification


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    
    ordering = ("email",)

    list_display = (
        "email",
        "first_name",
        "last_name",
        "role",
        "is_staff",
        "is_active",
        "is_email_verified",
    )

    search_fields = (
        "email",
        "first_name",
        "last_name",
        "role",
    )

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal Info", {"fields": ("first_name", "last_name", "role")}),
        ("Permissions", {
            "fields": (
                "is_active",
                "is_staff",
                "is_superuser",
                "is_email_verified",
                "groups",
                "user_permissions",
            )
        }),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "role",
                    "is_staff",
                    "is_active",
                    "is_email_verified",
                ),
            },
        ),
    )
    

@admin.register(PasswordResetRequest)
class PasswordResetRequestAdmin(admin.ModelAdmin):

    list_display = (
        "token",
        "user",
        "is_active",
        "expires_at",
        "created_at",
    )

    list_filter = (
        "is_active",
        "created_at",
    )

    search_fields = (
        "user__email",
        "token",
    )

    ordering = (
        "-created_at",
    )
    
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False
    

@admin.register(EmailVerification)
class EmailVerificationAdmin(admin.ModelAdmin):

    list_display = (
        "token",
        "user",
        "is_active",
        "expires_at",
        "created_at",
    )

    list_filter = (
        "is_active",
        "created_at",
    )

    search_fields = (
        "user__email",
        "token",
    )

    ordering = (
        "-created_at",
    )
    
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False
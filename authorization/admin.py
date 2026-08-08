from django.contrib import admin

from .models import Permission, Role


@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "code",
        "created_at",
    )

    search_fields = (
        "name",
        "code",
    )

    ordering = (
        "name",
    )


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "code",
        "created_at",
    )

    search_fields = (
        "name",
        "code",
    )

    filter_horizontal = (
        "permissions",
    )

    ordering = (
        "name",
    )
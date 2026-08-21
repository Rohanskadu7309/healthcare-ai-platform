from rest_framework.permissions import BasePermission


class HasRBACPermission(BasePermission):

    message = "You do not have permission to perform this action."

    def has_permission(self, request, view):

        required_permission = getattr(
            view,
            "required_permission",
            None,
        )

        if not required_permission:
            return False

        user = request.user

        if not user or not user.is_authenticated:
            return False

        if not user.role:
            return False

        return user.role.permissions.filter(
            codename=required_permission,
        ).exists()
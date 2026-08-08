from django.core.management.base import BaseCommand
from django.db import transaction

from authorization.constants import PERMISSIONS, ROLES
from authorization.models import Permission, Role


class Command(BaseCommand):

    help = "Create default RBAC permissions and roles."

    @transaction.atomic
    def handle(self, *args, **options):

        self.stdout.write(
            self.style.WARNING(
                "Seeding RBAC permissions and roles..."
            )
        )

        permissions = {}

        # Create or update permissions
        for code, data in PERMISSIONS.items():

            permission, created = Permission.objects.update_or_create(
                code=code,
                defaults={
                    "name": data["name"],
                    "description": data["description"],
                },
            )

            permissions[code] = permission

            if created:
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Created permission: {code}"
                    )
                )
            else:
                self.stdout.write(
                    f"Permission already exists: {code}"
                )

        # Create or update roles
        for code, data in ROLES.items():

            role, created = Role.objects.update_or_create(
                code=code,
                defaults={
                    "name": data["name"],
                    "description": data["description"],
                },
            )

            if data["permissions"] == "*":

                role.permissions.set(
                    permissions.values()
                )

            else:

                role.permissions.set(
                    [
                        permissions[permission_code]
                        for permission_code in data["permissions"]
                    ]
                )

            if created:
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Created role: {code}"
                    )
                )
            else:
                self.stdout.write(
                    f"Role already exists: {code}"
                )

        self.stdout.write(
            self.style.SUCCESS(
                "RBAC permissions and roles seeded successfully."
            )
        )
from django import forms
from django.contrib import admin

from .models import Patient

class UserModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        full_name = f"{obj.first_name} {obj.last_name}".strip()
        return full_name if full_name else obj.email

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    
    ordering = ("user",)
    
    list_display = (
        "patient_name",
        "date_of_birth",
        "gender",
        "blood_group",
        "phone_number",
        "created_at",
    )
    
    search_fields = (
        "user__first_name",
        "user__last_name",
    )
    
    list_filter = (
        "gender",
        "blood_group",
    )
    
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        
        return queryset.filter(user__role__name__iexact="Patient")
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):

        if db_field.name == "user":

            kwargs["queryset"] = (
                db_field.related_model.objects.filter(
                    role__name__iexact="Patient",
                    is_active=True,
                )
            )
            
            kwargs["form_class"] = UserModelChoiceField

        return super().formfield_for_foreignkey(
            db_field,
            request,
            **kwargs,
        )

    @admin.display(description="Patient Name")
    def patient_name(self, obj):
        full_name = (
            f"{obj.user.first_name} {obj.user.last_name}"
        ).strip()

        return full_name or obj.user.email
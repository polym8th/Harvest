from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.forms.widgets import CheckboxInput
from django.db import models
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    
    # Define field sections shown in the user edit form in the admin
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
        (
            "Custom fields",
            {"fields": ("is_creator",)},
        ),  # Custom field specific to this project
    )

    # Style boolean fields like 'is_creator' with a larger checkbox

    formfield_overrides = {
        models.BooleanField: {
            "widget": CheckboxInput(
                attrs={"style": "font-weight: bold; font-size: 30px;"}
            )
        },
    }

    # Define fields shown when adding a new user in the admin

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "first_name",
                    "last_name",
                    "password1",
                    "password2",
                    "is_creator",
                ),
            },
        ),
    )

    # Admin list display columns

    list_display = (
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "is_creator",
    )
    list_filter = ("is_staff", "is_superuser", "is_creator") 
    search_fields = ("email", "first_name", "last_name")  # Admin search
    ordering = ("email",)  # Default sort order


# Register the custom user model with its custom admin configuration

admin.site.register(CustomUser, CustomUserAdmin)

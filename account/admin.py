from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.forms.widgets import CheckboxInput
from django.db import models
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
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
        ("Custom fields", {"fields": ("is_creator",)}),
    )

    formfield_overrides = {
        models.BooleanField: {
            "widget": CheckboxInput(
                attrs={"style": "font-weight: bold; font-size: 30px;"}
            )
        },
    }

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

    list_display = (
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "is_creator",
    )
    list_filter = ("is_staff", "is_superuser", "is_creator")
    search_fields = ("email", "first_name", "last_name")
    ordering = ("email",)


admin.site.register(CustomUser, CustomUserAdmin)
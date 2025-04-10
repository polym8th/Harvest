from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import (
    gettext_lazy as _,
)  # For translatable error messages


class CustomUserManager(BaseUserManager):

    # Custom manager to handle user creation logic
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(
                _("The email must be set")
            )  # Enforce email requirement
        email = self.normalize_email(email)  # Standardize the email format
        user = self.model(email=email, **extra_fields)  # Create user instance
        user.set_password(password)  # Hash the password
        user.save()  # Save to database
        return user

    def create_superuser(self, email, password, **extra_fields):
        # Ensure required flags for superuser creation
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("The superuser must have is_staff=True"))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("The superuser must have is_superuser=True"))
        return self.create_user(email, password, **extra_fields)
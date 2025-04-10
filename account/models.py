from django.db import models
from .managers import CustomUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone


class CustomUser(AbstractBaseUser, PermissionsMixin):

    # Remove the default username field
    username = None

    # Use email as the unique identifier

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=135)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # Allows access to admin
    date_joined = models.DateTimeField(default=timezone.now)

    is_creator = models.BooleanField(default=False)  # Custom creator role

    # Use email for authentication instead of username

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = (
        []
    )  # No additional required fields when creating superusers

    # Attach custom manager for user creation logic

    objects = CustomUserManager()

    def __str__(self):
        return self.email  # Used in admin and debugging

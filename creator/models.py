
from django.db import models
from account.models import CustomUser
from django.utils import timezone


class Article(models.Model):
    title = models.CharField(max_length=255)  # Article title

    from django_ckeditor_5.fields import (
        CKEditor5Field,
    )  # Rich text field import

    content = CKEditor5Field(
        config_name="default"
    )
    pub_date = models.DateTimeField(
        auto_now_add=True
    )  # Set once when article is created

    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="creator_articles"
    )

    image = models.ImageField(
        upload_to="article_images/", null=True, blank=True
    )  # Optional image upload

    is_published = models.BooleanField(
        default=True
    )  # Show/hide article in public views

    article_teaser = models.BooleanField(
        default=False,
        help_text="Allow this article to be viewed without login",
    )  # If True, article is visible to guests

    created_at = models.DateTimeField(
        default=timezone.now
    )  # Create timestamp
    updated_at = models.DateTimeField(
        default=timezone.now
    )  # Last update timestamp

    # Tracks who last updated the article
    updated_by = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="updated_articles",
    )

    # ---- Event-specific fields ----

    is_event_related = models.BooleanField(
        default=False, help_text="Is this article related to an event?"
    )  # Option drop-down for creating an event.

    event_date = models.DateTimeField(null=True, blank=True)
    event_name = models.CharField(max_length=200, null=True, blank=True)
    event_venue = models.CharField(max_length=200, null=True, blank=True)
    event_location = models.CharField(max_length=200, null=True, blank=True)
    event_postcode = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.title  # Display article title in admin and queries

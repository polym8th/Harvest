from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget
from django.forms import ModelForm

from .models import Article
from account.models import CustomUser


class ArticleForm(ModelForm):
    # Rich text editor for article content
    content = forms.CharField(
        widget=CKEditor5Widget(config_name='default'),
        required=False  # Allow form submission even if hidden or optional
    )

    class Meta:
        model = Article
        fields = ["title", "content", "image"]
        labels = {"image": ""}  # Hide label for image field in the UI

    def save(self, commit=True, user=None):
        # Tracks who updated the article
        article = super().save(commit=False)
        if user:
            article.updated_by = user
        if commit:
            article.save()
        return article


class UpdateUserForm(ModelForm):
    # Form for updating user profile info
    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "email"]


class EventForm(ModelForm):
    # Form for managing event-related article data
    class Meta:
        model = Article
        fields = [
            "title", "content", "image",
            "event_date", "event_name", "event_venue",
            "event_location", "event_postcode"
        ]

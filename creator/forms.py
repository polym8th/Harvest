from django import forms
from .models import Article
from account.models import CustomUser
from django.forms import ModelForm
from django_ckeditor_5.widgets import CKEditor5Widget


class ArticleForm(forms.ModelForm):
    content = forms.CharField(
        widget=CKEditor5Widget(config_name='default'),
        required=False  # Avoid browser blocking submission on hidden field
    )

    class Meta:
        model = Article
        fields = ["title", "content", "image"]
        labels = {
            "image": "",
        }

    def save(self, commit=True, user=None):
        article = super().save(commit=False)
        if user:
            article.updated_by = user
        if commit:
            article.save()
        return article


class UpdateUserForm(ModelForm):
    password = None

    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "email"]
        exclude = ["password1", "password2"]

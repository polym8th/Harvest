from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from creator.models import Article
from django.forms import ModelForm


class CreateUserForm(UserCreationForm):
    is_creator = forms.BooleanField(required=False, label="Are you a content creator?")

    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2', 'is_creator']
        
class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'image']  # ✅ Removed 'is_unlimited'

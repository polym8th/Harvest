from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CreateUserForm(UserCreationForm):
    unlimited_access_membership = forms.BooleanField(required=False, label="Do you have unlimited access membership?")
    is_creator = forms.BooleanField(required=False, label="Are you a content creator?")

    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2', 'is_creator', 'unlimited_access_membership']

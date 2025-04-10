from django.forms import ModelForm
from account.models import CustomUser


class UpdateUserForm(ModelForm):
    # Form for updating basic user details
    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "email"]

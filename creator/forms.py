from .models import Article
from account.models import CustomUser
from django.forms import ModelForm

class ArticleForm(ModelForm):
    
    class Meta:
        model = Article
        fields = ['title', 'content', 'image']
        labels = {
            'image': '',
        }       

    def save(self, commit=True, user=None):  # Allow passing user parameter
        article = super().save(commit=False)

        # Always update 'updated_by' field when saving
        if user:
            article.updated_by = user

        if commit:
            article.save()
        return article
        
class UpdateUserForm(ModelForm):
    
    password = None

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email']    
        exclude = ['password1', 'password2']

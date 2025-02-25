from . models import Article

from account.models import CustomUser 

from django.forms import ModelForm


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'image']    

        
class UpdateUserForm(ModelForm):
    
    password = None
    class Meta:
        
        model = CustomUser
        fields = ['first_name', 'last_name', 'email',]    
        exclude = ['password1' , 'password2',]
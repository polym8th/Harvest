from django.db import models
from account.models import CustomUser

class Article(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(max_length=10000)
    pub_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='creator_articles')
    image = models.ImageField(upload_to='article_images/', null=True, blank=True)  # New ImageField
    is_published = models.BooleanField(default=True) 

    def __str__(self):
        return self.title

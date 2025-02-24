from django.db import models

from account.models import CustomUser

class Article(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(max_length=10000)
    pub_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustomUser, max_length=10, on_delete=models.CASCADE, null=True, related_name='client_articles')
    image = models.ImageField(upload_to='article_images/', null=True, blank=True)  # New ImageField

    def __str__(self):
        return self.title





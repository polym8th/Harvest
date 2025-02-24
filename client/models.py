from django.db import models

from account.models import CustomUser
class Membership(models.Model):

    member_name = models.CharField(max_length=300)

    membership_plan = models.CharField(max_length=255)
    membership_cost = models.CharField(max_length=255)

    is_active = models.BooleanField(default=False)

    user = models.OneToOneField(CustomUser, max_length=10, on_delete=models.CASCADE, unique=True)

    def __str__(self):

        return f'{self.member_name} - {self.membership_plan} membership'
class Article(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(max_length=10000)
    pub_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustomUser, max_length=10, on_delete=models.CASCADE, null=True, related_name='client_articles')
    image = models.ImageField(upload_to='article_images/', null=True, blank=True)  # New ImageField

    def __str__(self):
        return self.title





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
    title = models.CharField(max_length=255)
    content = models.TextField()
    pub_date = models.DateTimeField()
    is_unlimited = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    






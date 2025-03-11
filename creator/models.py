from django.db import models
from account.models import CustomUser
from django.utils import timezone  

class Article(models.Model):
   
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=10000)
    pub_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='creator_articles')
    image = models.ImageField(upload_to='article_images/', null=True, blank=True)  
    is_published = models.BooleanField(default=True) 
    article_teaser = models.BooleanField(default=False, help_text="Allow this article to be viewed without login")
    created_at = models.DateTimeField(default=timezone.now) 
    updated_at = models.DateTimeField(default=timezone.now) 
    updated_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='updated_articles')
    
    # Event-related fields
    is_event_related = models.BooleanField(default=False, help_text="Is this article related to an event?")
    event_date = models.DateTimeField(null=True, blank=True)
    event_name = models.CharField(max_length=200, null=True, blank=True)
    event_venue = models.CharField(max_length=200, null=True, blank=True)
    event_location = models.CharField(max_length=200, null=True, blank=True)
    event_postcode = models.CharField(max_length=10, null=True, blank=True)
    
    def __str__(self):
        return self.title

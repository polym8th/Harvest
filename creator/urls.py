from django.urls import path

from . import views

urlpatterns = [
    path('creator-dashboard', views.creator_dashboard, name="creator-dashboard"),
    
    path('create-article', views.create_article, name="create-article"),
    
    path('my-article', views.my_article, name="my-article"),


    
]
from django.urls import path

from . import views



urlpatterns = [
    path('creator-dashboard', views.creator_dashboard, name="creator-dashboard"),
    
    path('create-article', views.create_article, name="create-article"),
    
    path('published', views.published, name="published"),
    
    path('update-article/<str:pk>', views.update_article, name="update-article"),
    
    path('delete-article/<str:pk>', views.delete_article, name="delete-article"),
    
    path('manage-account', views.manage_account, name="manage-account"),
    

]
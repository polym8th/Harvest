from django.urls import path, include
from django.conf import settings  
from django.conf.urls.static import static 

from . import views

urlpatterns = [
    path('', views.creator_dashboard, name="creator-dashboard"),
    path('create-article/', views.create_article, name="create-article"),
    path('create-article-success/', views.create_article_success, name='create-article-success'),
    path('published/', views.published, name="published"),
    path('update-article/<str:pk>/', views.update_article, name="update-article"),
    path('delete-article/<str:pk>/', views.delete_article, name="delete-article"),
    path('manage-account/', views.manage_account, name="manage-account"),
    path('update-article-success/', views.update_article_success, name="update-article-success"),
    path('delete-success/', views.delete_success, name="delete-success"),
    path('delete-account/', views.delete_account, name="delete-account"),  
    path('delete-account-success/', views.delete_account_success, name="delete-account-success"),  
    path('article-guest/<str:pk>/', views.article_guest, name="article-guest"),
    path("ckeditor5/", include("django_ckeditor_5.urls")),  
]

# ✅ Ensure media files are served correctly in development mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static  # ✅ Import static

from . import views

urlpatterns = [
    path('creator-dashboard', views.creator_dashboard, name="creator-dashboard"),
    path('create-article', views.create_article, name="create-article"),
    path('published', views.published, name="published"),
    path('update-article/<str:pk>', views.update_article, name="update-article"),
    path('delete-article/<str:pk>', views.delete_article, name="delete-article"),
    path('manage-account', views.manage_account, name="manage-account"),
    path('update-success', views.update_success, name="update-success"),
    path('delete-success', views.delete_success, name="delete-success"),
    path('delete-account-success/', views.delete_account_success, name="delete-account-success"),  
    path('article/<str:pk>/', views.article_detail, name="article-detail"),
    path('delete-account/', views.delete_account, name="delete-account"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
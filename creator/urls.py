from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.creator_dashboard, name="creator-dashboard"),
    path("create-article/", views.create_article, name="create-article"),
    path(
        "create-article-success/",
        views.create_article_success,
        name="create-article-success",
    ),
    path("published/", views.published, name="published"),
    path(
        "update-article/<str:pk>/", views.update_article, name="update-article"
    ),
    path(
        "delete-article/<str:pk>/", views.delete_article, name="delete-article"
    ),
    path(
        "update-article-success/",
        views.update_article_success,
        name="update-article-success",
    ),
    path('event/update/<int:pk>/', views.update_event, name='update-event'),
    path('event/delete/<int:pk>/', views.delete_event, name='delete-event'),
    path("delete-success/", views.delete_success, name="delete-success"),
    path("article-guest/<str:pk>/", views.article_guest, name="article-guest"),
    path("ckeditor5/", include("django_ckeditor_5.urls")),
]

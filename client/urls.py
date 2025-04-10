
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path(
        "client-dashboard/", views.client_dashboard, name="client-dashboard"
    ),  # Dashboard for general users
    path(
        "regular-articles/", views.regular_articles, name="regular-articles"
    ),  # List of articles for general users
]

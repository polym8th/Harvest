from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('client-dashboard/', views.client_dashboard, name='client-dashboard'),
    path('regular-articles/', views.regular_articles, name='regular-articles'),
    path('manage-account-client/', views.manage_account, name='manage-account-client'),
    path('delete-account-client/', views.delete_account, name="delete-account-client"),
    path('delete-account-success/', views.delete_account_success, name="delete-account-success"),
]
from django.urls import path
from . import views

urlpatterns = [
    path('client-dashboard/', views.client_dashboard, name='client-dashboard'),
    path('regular-articles/', views.regular_articles, name='regular-articles'),
    path('manage-account/', views.manage_account, name='manage-account'),
]

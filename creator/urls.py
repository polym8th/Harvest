from django.urls import path

from . import views

urlpatterns = [
    path('creator-dashboard', views.creator_dashboard, name="creator-dashboard"),
    
]
from django.urls import path
from account import views

urlpatterns = [
    path("", views.home, name="home"),
    path("register", views.register, name="register"),
    path("my-login", views.my_login, name="my-login"),
    path("user-logout", views.user_logout, name="user-logout"),
    path(
        "manage-account/", views.manage_account, name="manage-account"
    ),
    path(
        "delete-account/", views.delete_account, name="delete-account"
    ),
    path(
        "delete-account-success/",
        views.delete_account_success,
        name="delete-account-success",
    ),  # Shown after account is deleted
]

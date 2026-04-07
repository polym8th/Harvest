from django.shortcuts import render, redirect
from django.contrib.auth import (
    authenticate,
    login,
    logout,
    update_session_auth_hash,
)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.db import OperationalError

from .forms import CreateUserForm
from creator.forms import UpdateUserForm
from creator.models import Article


def home(request):

    # Fetch 10 most recent published articles

    articles = Article.objects.filter(is_published=True).order_by("-pub_date")[
        :10
    ]
# Remove 'is_creator' flag so it is not displayed in the template

    for article in articles:
        if hasattr(article.user, "is_creator") and article.user.is_creator:
            article.user.is_creator = ""
    return render(request, "account/index.html", {"articles": articles})


def redirect_user_dashboard(user):

    # Redirect user to appropriate dashboard based on role

    if user.is_superuser or getattr(user, "is_creator", False):
        return redirect("creator-dashboard")
    return redirect("client-dashboard")


def register(request):

    # Redirect authenticated users to their dashboard
    if request.user.is_authenticated:
        return redirect_user_dashboard(request.user)
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            # Save new user with 'is_creator' flag if set

            user = form.save(commit=False)
            user.is_creator = form.cleaned_data.get("is_creator")
            user.save()

            # Show tailored success messages

            messages = [
                "Well done, your account has been created successfully!"
            ]
            if user.is_creator:
                messages.append("You are now a content creator!")
            return render(
                request,
                "account/registration_success.html",
                {"messages": messages},
            )
    else:
        form = CreateUserForm()
    return render(request, "account/register.html", {"RegisterForm": form})


def my_login(request):

    # Redirect already logged-in users

    if request.user.is_authenticated:
        return redirect_user_dashboard(request.user)
    error_message = None

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        try:
            if form.is_valid():
                username = form.cleaned_data.get("username")
                password = form.cleaned_data.get("password")
                user = authenticate(
                    request, username=username, password=password
                )

                if user is not None:
                    login(request, user)
                    return redirect_user_dashboard(user)
                else:
                    error_message = "Invalid username or password."
        except OperationalError:
            # Handle DB connection failure gracefully

            error_message = (
                "⚠️ Sorry, we're having trouble connecting to the database. "
                "Please check your internet connection and try again."
            )
    else:
        form = AuthenticationForm()
    return render(
        request,
        "account/my-login.html",
        {
            "LoginForm": form,
            "error_message": error_message,
        },
    )


@login_required(login_url="my-login")
def manage_account(request):

    # Allow users to update their account details

    user = request.user

    if request.method == "POST":
        form = UpdateUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(
                request, user
            )  # Keep session valid after password change
            messages.success(
                request, "✅ Your account details have been updated."
            )
            return redirect_user_dashboard(user)
    else:
        form = UpdateUserForm(instance=user)
    return render(
        request, "account/manage-account.html", {"UpdateUserForm": form}
    )


def user_logout(request):

    # Log the user out and return to home page

    logout(request)
    return redirect("home")


@login_required(login_url="my-login")
def delete_account(request):

    # Confirm account deletion

    if request.method == "POST":
        user = request.user
        user.delete()
        logout(request)
        return redirect("delete-account-success")
    return render(request, "account/delete-account.html")


def delete_account_success(request):

    # Show deletion confirmation screen

    return render(request, "account/delete-account-success.html")

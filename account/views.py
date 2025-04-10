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
    
    # Show latest 10 published articles on homepage
    if request.user.is_authenticated:
        articles = Article.objects.filter(is_published=True).order_by(
            "-pub_date"
        )[:10]
    else:
        articles = Article.objects.filter(is_published=True).order_by(
            "-pub_date"
        )[:10]
        
    # Clear 'is_creator' flag from user object (likely for display logic)
    for article in articles:
        if hasattr(article.user, "is_creator") and article.user.is_creator:
            article.user.is_creator = ""
    return render(request, "account/index.html", {"articles": articles})


def register(request):
    
    # Prevent access to registration if already logged in
    if request.user.is_authenticated:
        if request.user.is_superuser or request.user.is_creator:
            return redirect("creator-dashboard")
        return redirect("client-dashboard")
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            is_creator = form.cleaned_data.get("is_creator")
            user.is_creator = is_creator
            user.save()

            messages = [
                "Well done, your account has been created successfully!"
            ]
            if is_creator:
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
    
    # Prevent logged-in users from accessing login page
    if request.user.is_authenticated:
        if request.user.is_superuser or request.user.is_creator:
            return redirect("creator-dashboard")
        return redirect("client-dashboard")
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
                    if user.is_superuser or user.is_staff or user.is_creator:
                        return redirect("creator-dashboard")
                    else:
                        return redirect("client-dashboard")
                else:
                    error_message = "Invalid username or password."
        except OperationalError:
            # Handle potential DB or connection issues

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
    user = request.user  # Get the currently logged-in user
    form = UpdateUserForm(instance=user)  # Pre-fill form with user info

    if request.method == "POST":
        # Populate form with submitted data
        form = UpdateUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()  # Save updated user info
            update_session_auth_hash(request, user)  # Prevent logout
            messages.success(
                request,
                "✅ Your account details have been updated.",
            )

            # Redirect based on user role

            if user.is_superuser:
                return redirect("creator-dashboard")
            elif getattr(user, "is_creator", False):
                return redirect("creator-dashboard")
            else:
                return redirect("client-dashboard")
    return render(
        request,
        "account/manage-account.html",
        {"UpdateUserForm": form},
    )


def user_logout(request):
    logout(request)
    return redirect("home")


@login_required(login_url="my-login")
def delete_account(request):
    if request.method == "POST":
        user = request.user  # capture the user object before logout
        user.delete()  # delete user first
        logout(request)  # logout after
        return redirect("delete-account-success")
    return render(request, "account/delete-account.html")


def delete_account_success(request):
    return render(request, "account/delete-account-success.html")

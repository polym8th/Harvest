from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from creator.models import Article
from django.db import OperationalError


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
                "⚠️ Sorry, we're having trouble connecting to the database."
                " Please check your internet connection and try again."
            )
    else:
        form = AuthenticationForm()
    return render(
        request,
        "account/my-login.html",
        {"LoginForm": form, "error_message": error_message},
    )


def user_logout(request):
    # Log user out and redirect to home

    logout(request)
    return redirect("home")

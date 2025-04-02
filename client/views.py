from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from creator.models import Article
from django.contrib.auth.models import User
from .forms import UpdateUserForm


login_required(login_url="my-login")


def client_dashboard(request):
    if request.user.is_creator or request.user.is_superuser:
        raise PermissionDenied
    user_articles = Article.objects.filter(user=request.user)
    return render(
        request, "client/client-dashboard.html", {"articles": user_articles}
    )


@login_required(login_url="my-login")
def regular_articles(request):
    if request.user.is_creator or request.user.is_superuser:
        raise PermissionDenied
    # Fetch only published articles

    articles = Article.objects.filter(is_published=True)

    return render(
        request, "client/regular-articles.html", {"AllArticles": articles}
    )


@login_required(login_url="my-login")
def manage_account(request):
    if request.user.is_creator or request.user.is_superuser:
        raise PermissionDenied
    form = UpdateUserForm(instance=request.user)

    if request.method == "POST":
        form = UpdateUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Your account has been updated successfully!"
            )
            return redirect("client-dashboard")
    return render(
        request, "account/manage-account.html", {"UpdateUserForm": form}
    )


@login_required(login_url="my-login")
def delete_account(request):
    if request.method == "POST":
        user = request.user
        user.delete()
        return redirect("delete-account-success")
    return render(request, "account/delete-account.html")


def delete_account_success(request):
    return render(request, "account/delete-account-success.html")


@login_required(login_url="my-login")
def delete_success(request):
    return render(request, "account/delete-success.html")


@login_required(login_url="my-login")
def update_success(request):
    return render(request, "account/update-success.html")
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib import messages

from creator.models import Article
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
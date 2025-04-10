from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib import messages

from creator.models import Article
from .forms import UpdateUserForm


login_required(login_url="my-login")  # Misplaced — does nothing here


def client_dashboard(request):
    # Restrict access to non-creators and non-superusers
    if request.user.is_creator or request.user.is_superuser:
        raise PermissionDenied
    user_articles = Article.objects.filter(user=request.user)
    return render(
        request, "client/client-dashboard.html", {"articles": user_articles}
    )


@login_required(login_url="my-login")
def regular_articles(request):
    # Restrict creators and superusers from viewing this page
    if request.user.is_creator or request.user.is_superuser:
        raise PermissionDenied

    # Show only published articles to general users
    articles = Article.objects.filter(is_published=True)

    return render(
        request, "client/regular-articles.html", {"AllArticles": articles}
    )

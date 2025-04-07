from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.db.models import Q


from creator.forms import ArticleForm, UpdateUserForm, EventForm
from .models import Article


def index(request):
    teaser_articles = Article.objects.filter(
        article_teaser=True, is_published=True
    )
    for article in teaser_articles:
        if (
            hasattr(article, "article_teaser")
            and article.article_teaser is True
        ):
            article.article_teaser = ""
    return render(
        request, "accounts/index.html", {"teaser_articles": teaser_articles}
    )


@login_required(login_url="my-login")
def creator_dashboard(request):
    if not (request.user.is_creator or request.user.is_superuser):
        messages.error(
            request,
            "❌ Access denied. Creator or superuser permissions required.",
        )
        return redirect("client-dashboard")

    user_articles = Article.objects.filter(user=request.user)
    return render(
        request, "creator/creator-dashboard.html", {"articles": user_articles}
    )


@login_required(login_url="my-login")
def create_article(request):
    if not (request.user.is_creator or request.user.is_superuser):
        messages.error(request, "❌ You are not allowed to create articles.")
        return redirect("client-dashboard")

    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.article_teaser = (
                request.POST.get("article_teaser", "0") == "1"
            )
            article.is_event_related = (
                request.POST.get("is_event_related") == "on"
            )

            if article.is_event_related:
                article.event_date = request.POST.get("event_date")
                article.event_name = request.POST.get("event_name")
                article.event_venue = request.POST.get("event_venue")
                article.event_location = request.POST.get("event_location")
                article.event_postcode = request.POST.get("event_postcode")

            if "image" in request.FILES:
                uploaded_image = request.FILES["image"]
                print(
                    f"✅ Image Uploaded: {uploaded_image.name} | "
                    f"Size: {uploaded_image.size} bytes | "
                    f"Type: {uploaded_image.content_type}"
                )

            article.save()
            return redirect("create-article-success")
    else:
        form = ArticleForm()

    return render(
        request, "creator/create-article.html", {"CreateArticleForm": form}
    )


@login_required(login_url="my-login")
def create_article_success(request):
    if not (request.user.is_creator or request.user.is_superuser):
        messages.error(
            request,
            "Access denied. Creator or superuser permissions required.",
        )
        return redirect("client-dashboard")

    return render(request, "creator/create-article-success.html")


def article_guest(request, pk):
    article = get_object_or_404(Article, id=pk)
    return render(request, "account/article-guest.html", {"article": article})


@login_required(login_url="my-login")
def published(request):
    if not (request.user.is_creator or request.user.is_superuser):
        messages.error(
            request,
            "❌ Access denied. Creator or superuser permissions required.",
        )
        return redirect("client-dashboard")

    query = request.GET.get("query")
    articles = Article.objects.filter(
        Q(is_published=True) | Q(article_teaser=True)
    )

    if query:
        articles = articles.filter(
            Q(title__icontains=query) | Q(id__iexact=query)
        )
        if not articles.exists():
            messages.warning(
                request,
                f"No articles or events found matching: '{query}'"
            )
            return redirect("published")

    all_articles = articles.filter(is_event_related=False)
    events = articles.filter(is_event_related=True)

    return render(
        request,
        "creator/published.html",
        {
            "AllArticles": all_articles,
            "Events": events,
        },
    )


@login_required(login_url="my-login")
def update_article(request, pk):
    article = get_object_or_404(Article, id=pk)

    if not request.user.is_authenticated:
        messages.error(
            request, "❌ You don't have permission to update this article."
        )
        return redirect("my-login")

    if request.user.is_creator and article.user != request.user:
        messages.error(
            request,
            "❌ You cannot update this article if you did not create it.",
        )
        return redirect("published")

    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            article = form.save(commit=False)
            article.article_teaser = request.POST.get("article_teaser") == "1"
            article.updated_by = request.user
            article.updated_at = timezone.now()
            article.save()
            messages.success(
                request,
                "✅ Your article has been updated successfully!",
                extra_tags="update",
            )
            return redirect("published")
    else:
        form = ArticleForm(instance=article)

    return render(
        request,
        "creator/update-article.html",
        {"UpdateArticleForm": form, "article": article},
    )


@login_required(login_url="my-login")
def update_article_success(request):
    if request.user.is_authenticated:
        if request.user.is_superuser or request.user.is_creator:
            return redirect("creator-dashboard")
        return redirect("client-dashboard")

    return render(request, "creator/update-article-success.html")


@login_required(login_url="my-login")
def delete_article(request, pk):
    article = get_object_or_404(Article, id=pk)

    if not request.user.is_authenticated:
        messages.error(
            request, "❌ You don't have permission to delete this article."
        )
        return redirect("my-login")

    if request.user.is_creator and article.user != request.user:
        messages.error(
            request,
            "❌ You cannot delete this article if you did not create it.",
        )
        return redirect("published")

    if not (
        request.user.is_superuser
        or (request.user.is_creator and article.user == request.user)
    ):
        messages.error(
            request,
            "❌ You cannot delete this article if you did not create it.",
        )
        return redirect("client-dashboard")

    if request.method == "POST":
        article.delete()
        messages.success(request, "The article has been deleted successfully.")
        return redirect("published")

    return render(request, "creator/delete-success.html", {"article": article})


@login_required(login_url="my-login")
def delete_success(request):
    if request.user.is_authenticated:
        if request.user.is_superuser or request.user.is_creator:
            return redirect("creator-dashboard")


@login_required(login_url="my-login")
def update_event(request, pk):
    if not request.user.is_authenticated:
        messages.error(
            request, "❌ You don't have permission to update this event."
        )
        return redirect("my-login")

    event = get_object_or_404(Article, pk=pk, is_event_related=True)

    if request.user.is_creator and event.user != request.user:
        messages.error(
            request,
            "❌ You cannot update this event if you did not create it.",
        )
        return redirect("published")

    if request.method == "POST":
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Event updated successfully.")
            return redirect("published")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = EventForm(instance=event)

    return render(
        request, "creator/edit-event.html", {"form": form, "event": event}
    )


@login_required(login_url="my-login")
def delete_event(request, pk):
    if not request.user.is_authenticated:
        messages.error(
            request, "❌ You don't have permission to delete this event."
        )
        return redirect("my-login")

    event = get_object_or_404(Article, pk=pk, is_event_related=True)

    if request.user.is_creator and event.user != request.user:
        messages.error(
            request,
            "❌ You cannot delete this event if you did not create it.",
        )
        return redirect("published")

    if request.method == "POST":
        event.delete()
        messages.success(request, "✅ Event deleted successfully.")
        return redirect("published")

    messages.error(request, "❌ Invalid request.")
    return redirect("published")

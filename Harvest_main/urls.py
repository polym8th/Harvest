from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "", include("account.urls")
    ),  # Root URL routes to account app (e.g., homepage, login)
    path("client/", include("client.urls")),
    path("creator/", include("creator.urls")),
    path(
        "accounts/", include("django.contrib.auth.urls")
    ),  
]

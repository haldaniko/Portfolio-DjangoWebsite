from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("website.urls", namespace="website")),
]
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

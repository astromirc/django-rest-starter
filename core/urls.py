from django.conf import settings
from django.contrib import admin
from django.urls import path

# Urls
urlpatterns = []

if settings.DEBUG:
    from django.conf.urls.static import static

    # Django admin
    urlpatterns += [
        path("admin/", admin.site.urls),
    ]

    # Media files
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

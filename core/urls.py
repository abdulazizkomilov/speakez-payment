from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from django.contrib.auth.decorators import user_passes_test
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)


def is_superuser(user):
    return user.is_superuser


def health_check(request):
    return JsonResponse({"status": "healthy"}, status=200)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", health_check),
    path(
        "api/",
        include(
            [
                path("payme/", include("payment.urls")),
                path("schema/site/", user_passes_test(is_superuser)(SpectacularAPIView.as_view()), name="schema"),
                path(
                    "swagger/site/",
                    user_passes_test(is_superuser)(SpectacularSwaggerView.as_view(url_name="schema")),
                    name="swagger-ui",
                ),
                path(
                    "redoc/site/",
                    user_passes_test(is_superuser)(SpectacularRedocView.as_view(url_name="schema")),
                    name="redoc",
                ),
            ]
        ),
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

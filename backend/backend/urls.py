import os
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from API.schema.schema import schema_view


urlpatterns = [
    path("admin/", admin.site.urls),
    path(f"{settings.BASE_API_URL}/list/", include("API.urls")),
    path(f"{settings.BASE_API_URL}/auth/", include("users.urls")),
    path(f"{settings.BASE_API_URL}/profile/", include("profiles.urls")),
    path(f"{settings.BASE_API_URL}/order/", include("order.urls")),
    path(
        "api/docs/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        "api/redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
    ),
    path("smsru/", include("smsru.urls")),
    path("telegram/", include("telegram.urls")),
    path(f"{settings.BASE_API_URL}/review/", include("reviews.urls")),
    path("ckeditor5/", include("django_ckeditor_5.urls")),
    path(f"{settings.BASE_API_URL}/test/", include("sitedb.urls")),
    # path("adminpanel/", include("AdminPanel.urls")),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

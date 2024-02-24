from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from API.schema.schema import schema_view


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/list/", include("API.urls")),
    path("api/v1/auth/", include("users.urls")),
    path("api/v1/profile/", include("profiles.urls")),
    path("api/v1/order/", include("order.urls")),
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
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

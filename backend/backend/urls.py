from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from ProductAPI.schema.schema import schema_view
from database.views import create_products

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/product/", include("ProductAPI.urls")),
    path("api/auth/", include("users.urls")),
    path("api/profile/", include("profiles.urls")),
    path(
        "api/docs/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        "api/redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
    ),
    path("create/", create_products),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

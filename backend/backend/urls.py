import os
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from API.schema.schema import schema_view


urlpatterns = [
    path("admin/", admin.site.urls),
    path(f"api/{settings.API_VERSION}/product/", include("API.urls")),
    path(f"api/{settings.API_VERSION}/auth/", include("users.urls")),
    path(f"api/{settings.API_VERSION}/users/", include("profiles.urls")),
    path(f"api/{settings.API_VERSION}/order/", include("order.urls")),
    path(f"api/{settings.API_VERSION}/reviews/", include("reviews.urls")),
    path(f"api/{settings.API_VERSION}/site/", include("sitedb.urls")),
    path(f"api/{settings.API_VERSION}/vacancy/", include("vacancy.urls")),
    path(
        "api/docs/",
        schema_view.with_ui("swagger"),
        name="schema-swagger-ui",
    ),
    path("api/redoc/", schema_view.with_ui("redoc"), name="schema-redoc"),
    path("smsru/", include("smsru.urls")),
    path("telegram/", include("telegram.urls")),
    path("ckeditor5/", include("django_ckeditor_5.urls")),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.conf import settings
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_swagger.views import get_swagger_view

schema_view = get_schema_view(
    openapi.Info(
        title="Документация REST API(DRF)",
        default_version="v1.0.0",
        description="Документация пользовнаия API",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    # url=settings.SITE_URL,
)


test_view = get_swagger_view(title="Pastebin API")

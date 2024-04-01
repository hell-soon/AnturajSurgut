from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
   openapi.Info(
      title="Документация для REST API(DRF)",
      default_version='v1.0.0',
      description="Инструкция пользовнаия API",
   ),
   public=True,
)
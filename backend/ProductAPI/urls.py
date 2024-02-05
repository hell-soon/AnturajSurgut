from django.conf import settings
from django.urls.conf import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import routers

from .schema.schema import schema_view
from .views import CatalogViewSet, SubCatalogViewSet, SizeViewSet, ValueViewSet, ProductViewSet, TagsViewSet

router = routers.DefaultRouter()
router.register(r'catalogs', CatalogViewSet)
router.register(r'subcatalogs', SubCatalogViewSet)
router.register(r'sizes', SizeViewSet)
router.register(r'values', ValueViewSet)
router.register(r'tags', TagsViewSet)
router.register(r'products', ProductViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
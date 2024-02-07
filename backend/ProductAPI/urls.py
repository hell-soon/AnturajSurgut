from django.urls.conf import include, path

from rest_framework import routers

from .views import (
    CatalogViewSet,
    SubCatalogViewSet,
    SizeViewSet,
    ProductViewSet,
    TagsViewSet,
)

router = routers.DefaultRouter()
router.register(r"catalogs", CatalogViewSet)
router.register(r"subcatalogs", SubCatalogViewSet)
router.register(r"sizes", SizeViewSet)
router.register(r"tags", TagsViewSet)
router.register(r"products", ProductViewSet)


urlpatterns = [
    path("", include(router.urls)),
]

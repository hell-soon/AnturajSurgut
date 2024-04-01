from rest_framework import routers
from API.Views.Catalog.catalog import CatalogViewSet


router = routers.DefaultRouter()
router.register(r"catalog", CatalogViewSet)

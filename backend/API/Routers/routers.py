from rest_framework import routers
from API.Views.SubCatalogs import SubCatalogViewSet
from API.Views.Product import ProductViewSet
from API.Views.Catalogs import CatalogViewSet
from API.Views.Order import OrderViewSet
from API.Views.Tags import TagsViewSet


router = routers.DefaultRouter()
router.register(r"subcatalog", SubCatalogViewSet)
router.register(r"list", ProductViewSet)
router.register(r"catalog", CatalogViewSet)
router.register(r"order", OrderViewSet)
router.register(r"tags", TagsViewSet)

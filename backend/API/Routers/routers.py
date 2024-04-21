from rest_framework import routers
from API.Views.SubCatalog.SubCatalog import SubCatalogViewSet
from API.Views.Product.Product import ProductViewSet
from API.Views.Catalog.catalog import CatalogViewSet
from API.Views.Order.Order import OrderViewSet
from API.Views.Tags.TagsView import TagsViewSet


router = routers.DefaultRouter()
router.register(r"subcatalog", SubCatalogViewSet)
router.register(r"product", ProductViewSet)
router.register(r"catalog", CatalogViewSet)
router.register(r"order", OrderViewSet)
router.register(r"tags", TagsViewSet)

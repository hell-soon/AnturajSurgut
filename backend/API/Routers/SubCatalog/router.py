from rest_framework import routers
from API.Views.SubCatalog.SubCatalog import SubCatalogViewSet


router = routers.DefaultRouter()
router.register(r"subcatalog", SubCatalogViewSet)

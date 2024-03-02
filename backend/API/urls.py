from django.urls import path, include
from .views import (
    ProductViewSet,
    ProductInfoView,
    CatalogViewSet,
    SubCatalogViewSet,
    OrderViewSet,
    OrderInfoView,
)
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r"product", ProductViewSet)
router.register(r"catalog", CatalogViewSet)
router.register(r"subcatalog", SubCatalogViewSet)
router.register(r"order", OrderViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path(
        "product/info/<int:product_id>/", ProductInfoView.as_view(), name="product-info"
    ),
    path("order-info/<str:order_number>/", OrderInfoView.as_view(), name="order-info"),
]

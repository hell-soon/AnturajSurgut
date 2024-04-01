from django.urls import path, include

from .Views.Order.OrderInfo.OrderInfo import OrderInfoView
from .Views.Product.ProductInfo.ProductInfo import ProductInfoView
from .Routers.Product.router import router as product_router
from .Routers.Catalog.router import router as catalog_router
from .Routers.SubCatalog.router import router as subcatalog_router
from .Routers.Order.router import router as order_router


urlpatterns = [
    path("", include(product_router.urls)),
    path("", include(catalog_router.urls)),
    path("", include(subcatalog_router.urls)),
    path("", include(order_router.urls)),
    path(
        "product/info/<int:product_id>/", ProductInfoView.as_view(), name="product-info"
    ),
    path("order-info/<str:order_number>/", OrderInfoView.as_view(), name="order-info"),
]

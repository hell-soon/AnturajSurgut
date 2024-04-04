from django.urls import path, include

from .Views.Order import OrderInfoView
from .Views.Product import ProductInfoView
from .Routers.routers import router


urlpatterns = [
    path("", include(router.urls)),
    path(
        "product/info/<int:product_id>/", ProductInfoView.as_view(), name="product-info"
    ),
    path("order-info/<str:order_number>/", OrderInfoView.as_view(), name="order-info"),
]

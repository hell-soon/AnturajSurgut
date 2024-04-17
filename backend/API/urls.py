from django.urls import path, include

from .Views.Order import OrderInfoView
from .Views.Product import ProductInfoView, GlobalSearch
from .Routers.routers import router
from DB.models import Product, SubCatalog


urlpatterns = [
    path("", include(router.urls)),
    path(
        "product/info/<int:product_id>/", ProductInfoView.as_view(), name="product-info"
    ),
    path("order-info/<str:order_number>/", OrderInfoView.as_view(), name="order-info"),
    path("search/", GlobalSearch.as_view()),
]

from django.urls import path, include

from .Views.Order import OrderInfoView
from .Views.Product import ProductInfoView, GlobalSearch
from .Views.FilterMenu.FilterMenu import FilterMenu
from .Routers.routers import router


urlpatterns = [
    path("", include(router.urls)),
    path(
        "product/info/<int:product_id>/", ProductInfoView.as_view(), name="product-info"
    ),
    path("order-info/<str:order_number>/", OrderInfoView.as_view(), name="order-info"),
    path("search/", GlobalSearch.as_view()),
    path("filters/", FilterMenu.as_view()),
]

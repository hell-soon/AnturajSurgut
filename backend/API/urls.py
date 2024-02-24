from django.urls import path, include
from .views import ProductViewSet, ProductInfoView
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r"product", ProductViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path(
        "product/info/<int:product_id>/", ProductInfoView.as_view(), name="product-info"
    ),
]

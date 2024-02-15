from django.urls import path
from .views import (
    user_info,
    add_to_favorite,
    remove_from_favorite,
    CartView,
    add_to_cart,
    remove_from_cart,
)


urlpatterns = [
    path("info/", user_info, name="user_info"),
    path("favorite/add/", add_to_favorite, name="add_to_favorite"),
    path("favorite/remove/", remove_from_favorite, name="remove_from_favorite"),
    path("cart/", CartView.as_view(), name="cart"),
    path("add-to-cart/", add_to_cart, name="add_to_cart"),
    path("remove-from-cart/", remove_from_cart, name="remove_from_cart"),
]

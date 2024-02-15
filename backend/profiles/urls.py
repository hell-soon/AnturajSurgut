from django.urls import path
from .views import (
    user_info,
    add_to_favorite,
    remove_from_favorite,
    CartListCreateView,
    UserCartView,
)


urlpatterns = [
    path("info/", user_info, name="user_info"),
    path("favorite/add/", add_to_favorite, name="add_to_favorite"),
    path("favorite/remove/", remove_from_favorite, name="remove_from_favorite"),
    path("cart/", CartListCreateView.as_view()),
    path("test/", UserCartView.as_view()),
]

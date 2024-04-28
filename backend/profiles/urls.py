from django.urls import path
from .views import UserInfoViewSet


urlpatterns = [
    path(
        "profile/",
        UserInfoViewSet.as_view({"get": "current", "patch": "update"}),
        name="profile",
    ),
    path(
        "profile/review/",
        UserInfoViewSet.as_view({"get": "review", "post": "review_create"}),
        name="review",
    ),
    path(
        "profile/review/<int:pk>/",
        UserInfoViewSet.as_view(
            {
                "get": "review_detail",
                "patch": "update_review",
                "delete": "review_delete",
            }
        ),
        name="review_detail",
    ),
    path("profile/orders/", UserInfoViewSet.as_view({"get": "orders"}), name="orders"),
    path(
        "profile/orders/<int:pk>/",
        UserInfoViewSet.as_view({"get": "order_info"}),
        name="order_info",
    ),
]

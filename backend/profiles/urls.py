from django.urls import path
from .views import tg_order_buttons, UserInfoViewSet


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
    path("tg/", tg_order_buttons, name="tg_view"),
]

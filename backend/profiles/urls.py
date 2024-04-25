from django.urls import path, include
from .views import tg_order_buttons, UserInfoViewSet
from rest_framework import routers

router = routers.SimpleRouter()

# router.register("profile", UserInfoViewSet)

urlpatterns = [
    path("", include(router.urls)),
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
        name="review",
    ),
    path("tg/", tg_order_buttons, name="tg_view"),
]

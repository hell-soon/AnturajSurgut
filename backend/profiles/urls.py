from django.urls import path
from .views import update_user_view, UserInfoView, tg_order_buttons


urlpatterns = [
    path("change/", update_user_view, name="user_change"),
    path("info/", UserInfoView.as_view()),
    path("tg/", tg_order_buttons),
]

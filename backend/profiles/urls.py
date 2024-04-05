from django.urls import path
from .views import update_user_view, get_user_by_tg_id, UserInfoView


urlpatterns = [
    path("change/", update_user_view, name="user_change"),
    path("user/<int:tg_id>/", get_user_by_tg_id, name="user_by_tg_id"),
    path("info/", UserInfoView.as_view()),
]

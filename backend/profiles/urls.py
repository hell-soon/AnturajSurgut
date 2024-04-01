from django.urls import path
from .views import user_info, update_user_view, get_user_by_tg_id


urlpatterns = [
    path("info/", user_info, name="user_info"),
    path("change/", update_user_view, name="user_change"),
    path("user/<int:tg_id>/", get_user_by_tg_id, name="user_by_tg_id"),
]

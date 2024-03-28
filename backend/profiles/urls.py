from django.urls import path
from .views import user_info, update_user_view


urlpatterns = [
    path("info/", user_info, name="user_info"),
    path("change/", update_user_view, name="user_change"),
]

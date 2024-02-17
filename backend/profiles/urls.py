from django.urls import path
from .views import (
    user_info,
)


urlpatterns = [
    path("info/", user_info, name="user_info"),
]

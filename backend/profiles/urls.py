from django.urls import path
from .views import user_info, change_info


urlpatterns = [
    path("info/", user_info, name="user_info"),
    path("change/", change_info, name="user_change"),
]

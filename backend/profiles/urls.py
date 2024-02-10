from django.urls import path
from .views import user_info, add_to_favorite


urlpatterns = [
    path("info/", user_info, name="user_info"),
    path("favorite/", add_to_favorite, name="add_to_favorite"),
]

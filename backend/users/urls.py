from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from .views import (
    register_user,
    user_login_view,
    change_password,
    email_for_change_pass,
)

"""
ENDPOINTS FOR AUTHENTICATION
"""
urlpatterns = [
    path("register/", register_user, name="register"),
    path("login/", user_login_view, name="user_login"),
    path("change/password/", email_for_change_pass, name="password_change_email"),
    path(
        "change/password/<str:uid64>/<str:token>/",
        change_password,
        name="change_password",
    ),
    path("refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"),
]

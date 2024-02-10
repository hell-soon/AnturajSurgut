from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from .views import register_user, UserLoginView

urlpatterns = [
    path("register/", register_user, name="register"),
    path("login/", UserLoginView.as_view(), name="user_login"),
    path("refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"),
]

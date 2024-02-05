from django.urls import path

from .views import register_user, UserLoginView

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', UserLoginView.as_view(), name='user_login'),
]

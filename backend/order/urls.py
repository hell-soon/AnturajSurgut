from django.urls import path
from .views import create_order

urlpatterns = [
    path("create/", create_order, name="create_order"),
]

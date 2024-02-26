from django.urls import path
from .views import create_order, update_order, get_additional_services

urlpatterns = [
    path("service/", get_additional_services, name="get_additional_services"),
    path("create/", create_order, name="create_order"),
    path("update/<str:order_number>/", update_order, name="update_order"),
]

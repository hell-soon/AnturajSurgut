from django.urls import path
from .views import (
    create_order,
    get_additional_services,
    order_utils,
)

urlpatterns = [
    path("service/", get_additional_services, name="get_additional_services"),
    path("create/", create_order, name="create_order"),
    path("types/", order_utils),
]

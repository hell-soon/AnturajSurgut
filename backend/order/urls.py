from django.urls import path
from .views import (
    create_order,
    update_order,
    get_additional_services,
    order_utils,
)
from .Payment.Optional.Create.CreateOptionalPayment import create_peyment, check_payment
from .Payment.Optional.Refund.RefundOptionalPayment import refund_payment

urlpatterns = [
    path("service/", get_additional_services, name="get_additional_services"),
    path("create/", create_order, name="create_order"),
    path("update/<str:order_number>/", update_order, name="update_order"),
    path("payment/<str:order_number>/", create_peyment, name="create_peyment"),
    path("check/<str:payment_id>/", check_payment, name="check_payment"),
    path(
        "refund/<str:order_number>/",
        refund_payment,
        name="refund_payment",
    ),
    path("test/", order_utils, name="test"),
]

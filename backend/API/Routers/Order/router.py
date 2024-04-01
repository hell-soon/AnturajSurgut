from rest_framework import routers
from API.Views.Order.OrderView.Order import OrderViewSet

router = routers.DefaultRouter()
router.register(r"order", OrderViewSet)

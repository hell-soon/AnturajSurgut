from rest_framework import routers
from API.Views.Product.AllProduct.Product import ProductViewSet

router = routers.DefaultRouter()
router.register(r"product", ProductViewSet)

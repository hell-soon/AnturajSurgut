from rest_framework import routers
from .views import *
from django.urls import path
from django.urls import include

router = routers.DefaultRouter()
router.register(r"slider", SliderViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

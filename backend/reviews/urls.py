from django.urls import path, include
from .views import feedback, ReviewsViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r"review", ReviewsViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("feedback/", feedback, name="feedback"),
]

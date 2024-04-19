from django.urls import path, include
from .views import feedback, ReviewsViewSet, review_create, update_review, delete_review
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r"review", ReviewsViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("create/", review_create),
    path("update/<int:review_id>", update_review),
    path("delete/<int:review_id>", delete_review),
    path("feedback/", feedback, name="feedback"),
]

from django.urls import path

from .views import *


urlpatterns = [
    path("list/", VacancyViewSet.as_view({"get": "list"})),
    path(
        "list/<int:pk>/", VacancyViewSet.as_view({"post": "respond", "get": "retrieve"})
    ),
]

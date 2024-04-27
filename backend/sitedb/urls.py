from rest_framework import routers
from .views import *
from django.urls import path
from django.urls import include


urlpatterns = [
    path("slider/", SliderViewSet.as_view({"get": "list"})),
    path("contact/", ContactViewSet.as_view({"get": "list"})),
]

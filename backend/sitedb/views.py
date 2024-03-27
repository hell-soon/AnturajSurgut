from django.shortcuts import render
from .serializers.test import *
from .models import Slider

# Create your views here.
from rest_framework import viewsets

from .models import Sertificate
from icecream import ic
from django.utils import timezone


class SliderViewSet(viewsets.ModelViewSet):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer
    http_method_names = ["get"]

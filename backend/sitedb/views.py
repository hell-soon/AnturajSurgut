from rest_framework import viewsets
from .serializers.slider import SliderSerializer
from .models import Slider


class SliderViewSet(viewsets.ModelViewSet):
    queryset = Slider.objects.filter(is_active=True)
    serializer_class = SliderSerializer
    http_method_names = ["get"]

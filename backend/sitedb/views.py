from rest_framework import viewsets, status
from .serializers.slider import SliderSerializer
from rest_framework.response import Response
from .models import (
    Slider,
    Contact,
    SocialAccount,
    Service,
    Requisites,
    Address,
    WokrTime,
)
from .serializers.info import (
    ContactSerializer,
    FullInfoSerializer,
    FooterSerializer,
)
from .serializers.service import (
    ServiceSerializer,
    PreviewServiceSerializer,
)

from icecream import ic


class SliderViewSet(viewsets.ModelViewSet):
    queryset = Slider.objects.filter(is_active=True).order_by("-created_at")
    serializer_class = SliderSerializer
    http_method_names = ["get"]


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    http_method_names = ["get"]

    def get_object(self) -> Contact | None:
        # Получаем один объект Contact
        return Contact.objects.first()

    def list(self, request, *args, **kwargs):
        full_info = request.query_params.get("full_info", "false").lower() == "true"
        include_social = (
            request.query_params.get("include_social", "false").lower() == "true"
        )

        contact = self.get_object()
        response_data = {"contact": ContactSerializer(contact).data}

        if include_social:
            social_accounts = SocialAccount.objects.all()
            address = Address.objects.first()
            data = {
                "contact": contact,
                "social_accounts": social_accounts,
                "address": address,
            }
            serializer = FooterSerializer(data)
            return Response(serializer.data)

        if full_info:
            requisites = Requisites.objects.first()
            address = Address.objects.first()
            work_time = WokrTime.objects.first()
            data = {
                "contact": contact,
                "requisites": requisites,
                "address": address,
                "work_time": work_time,
            }
            serializer = FullInfoSerializer(data)
            return Response(serializer.data)

        return Response(response_data)



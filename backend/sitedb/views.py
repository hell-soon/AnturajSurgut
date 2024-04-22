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
    SocialAccountSerializer,
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


class ServiceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Service.objects.filter(is_active=True)
    serializer_class = ServiceSerializer

    def list(self, request, *args, **kwargs):
        preview = request.query_params.get("preview", "").lower() in ["true", "1"]
        services = self.get_queryset()

        if preview:
            service_serializer = PreviewServiceSerializer(services, many=True)
        else:
            service_serializer = self.get_serializer(services, many=True)

        response_data = {"services": service_serializer.data}

        return Response(response_data)


class V2ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.filter(is_active=True)
    serializer_class = ServiceSerializer
    http_method_names = ["get"]

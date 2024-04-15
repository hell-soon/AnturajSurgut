from rest_framework import viewsets
from .serializers.slider import SliderSerializer
from rest_framework.response import Response
from .models import Slider, Contact, SocialAccount, Service
from .serializers.info import SocialAccountSerializer, ContactSerializer
from .serializers.service import ServiceSerializer, PreviewServiceSerializer


class SliderViewSet(viewsets.ModelViewSet):
    queryset = Slider.objects.filter(is_active=True).order_by("-created_at")
    serializer_class = SliderSerializer
    http_method_names = ["get"]


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def list(self, request, *args, **kwargs):
        include_social = (
            request.query_params.get("include_social", "false").lower() == "true"
        )
        contacts = self.get_queryset()
        contact_serializer = self.get_serializer(contacts, many=True)
        response_data = {"contacts": contact_serializer.data}

        if include_social:
            social_accounts = SocialAccount.objects.all()
            social_serializer = SocialAccountSerializer(social_accounts, many=True)
            response_data["social_accounts"] = social_serializer.data

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

from rest_framework import viewsets, generics
from .serializers.slider import SliderSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import Slider, Contact, SocialAccount
from .serializers.info import SocialAccountSerializer, ContactSerializer


class SliderViewSet(viewsets.ModelViewSet):
    queryset = Slider.objects.filter(is_active=True)
    serializer_class = SliderSerializer
    http_method_names = ["get"]


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    http_method_names = ["get"]

    def list(self, request, *args, **kwargs):
        contacts = Contact.objects.all()
        contact_serializer = ContactSerializer(contacts, many=True)
        response_data = {
            "contacts": contact_serializer.data,
        }

        if (
            request.query_params.get("include_social").lower() == "true"
            or request.query_params.get("include_social") == "1"
        ):
            social_accounts = SocialAccount.objects.all()
            social_serializer = SocialAccountSerializer(social_accounts, many=True)
            response_data["social_accounts"] = social_serializer.data

        return Response(response_data)

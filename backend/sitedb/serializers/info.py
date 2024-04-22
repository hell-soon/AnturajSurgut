from rest_framework import serializers
from django.conf import settings
from sitedb.models import Contact, SocialAccount, Requisites, Address, WokrTime


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ["phone", "fax", "email"]


class SocialAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialAccount
        fields = ["name", "url", "icon"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        icon_url = representation.get("icon")
        if icon_url:
            full_icon_url = f"{settings.SITE_URL}{icon_url}"
            representation["icon"] = full_icon_url

        return representation


class RequisitesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Requisites
        fields = ["ip", "inn", "legal_address"]


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = ["address", "longitude", "latitude"]


class WokrTimeSerializer(serializers.ModelSerializer):

    class Meta:
        model = WokrTime
        fields = ["work_time"]


class FullInfoSerializer(serializers.Serializer):
    contact = ContactSerializer()
    address = AddressSerializer()
    requisites = RequisitesSerializer()
    work_time = WokrTimeSerializer()

    class Meta:
        fields = [
            "contact",
            "address",
            "requisites",
            "work_time",
        ]


class FooterSerializer(serializers.Serializer):
    contact = ContactSerializer()
    address = AddressSerializer()
    social_accounts = SocialAccountSerializer(many=True)

    class Meta:
        fields = [
            "contact",
            "address",
            "social_accounts",
        ]

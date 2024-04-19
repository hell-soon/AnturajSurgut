from rest_framework import serializers

from sitedb.models import Contact, SocialAccount, Requisites, Address, WokrTime


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ["phone", "fax", "email"]


class SocialAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialAccount
        fields = ["name", "url", "icon"]


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
    contact = ContactSerializer(many=True)
    # social_accounts = SocialAccountSerializer(many=True)
    requisites = RequisitesSerializer()
    address = AddressSerializer()
    work_time = WokrTimeSerializer()

    class Meta:
        fields = [
            "contact",
            # "social_accounts",
            "requisites",
            "address",
            "work_time",
        ]


class FooterSerializer(serializers.Serializer):
    contact = ContactSerializer(many=True)
    address = AddressSerializer()
    social_accounts = SocialAccountSerializer(many=True)

    class Meta:
        fields = [
            "contact",
            "address",
            "social_accounts",
        ]

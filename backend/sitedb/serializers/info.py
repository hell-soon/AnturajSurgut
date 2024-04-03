from rest_framework import serializers

from sitedb.models import Contact, SocialAccount


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"


class SocialAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialAccount
        fields = ["name", "url", "icon"]

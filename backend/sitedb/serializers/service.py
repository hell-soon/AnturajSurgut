from rest_framework import serializers
from sitedb.models import Service, ServiceSlider, ServiceOurWork, SiteImage, OurWork


# Сериализатор для SiteImage
class SiteImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteImage
        fields = ["image"]


# Сериализатор для OurWork
class OurWorkSerializer(serializers.ModelSerializer):
    image = SiteImageSerializer(many=True)

    class Meta:
        model = OurWork
        fields = ["id", "image"]


class ServiceOurWorkSerializer(serializers.ModelSerializer):
    our_work = OurWorkSerializer()

    class Meta:
        model = ServiceOurWork
        fields = ["our_work"]


# Сериализатор для ServiceSlider
class ServiceSliderSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = ServiceSlider
        fields = ["image"]

    def get_image(self, obj):
        request = self.context.get("request")
        image = obj.site_image.image.url
        return request.build_absolute_uri(image)


class ServiceSerializer(serializers.ModelSerializer):
    sliders = ServiceSliderSerializer(
        source="serviceslider_set", many=True, read_only=True
    )
    our_works = ServiceOurWorkSerializer(
        source="serviceourwork_set", many=True, read_only=True
    )

    class Meta:
        model = Service
        fields = [
            "id",
            "name",
            "text",
            "image",
            "sliders",
            "our_works",
        ]

    def to_representation(self, instance):
        data = super().to_representation(instance)

        if not instance.our_work_is_active:
            data.pop("our_works", None)

        return data


class PreviewServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = ["id", "name", "image"]

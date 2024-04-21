from rest_framework.response import Response
from rest_framework.views import APIView

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from DB.models import Color, Size, Compound
from API.serializers.MenuSerializers import MenuSerializer


class FilterMenu(APIView):
    @swagger_auto_schema(
        responses={
            200: openapi.Response(
                description="Фильтры",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "color": openapi.Schema(
                            type=openapi.TYPE_ARRAY,
                            items=openapi.Schema(
                                type=openapi.TYPE_OBJECT,
                                properties={
                                    "id": openapi.Schema(type=openapi.TYPE_INTEGER),
                                    "name": openapi.Schema(type=openapi.TYPE_STRING),
                                    "color": openapi.Schema(type=openapi.TYPE_STRING),
                                },
                            ),
                        ),
                        "size": openapi.Schema(
                            type=openapi.TYPE_ARRAY,
                            items=openapi.Schema(
                                type=openapi.TYPE_OBJECT,
                                properties={
                                    "id": openapi.Schema(type=openapi.TYPE_INTEGER),
                                    "name": openapi.Schema(type=openapi.TYPE_STRING),
                                },
                            ),
                        ),
                        "compound": openapi.Schema(
                            type=openapi.TYPE_ARRAY,
                            items=openapi.Schema(
                                type=openapi.TYPE_OBJECT,
                                properties={
                                    "id": openapi.Schema(type=openapi.TYPE_INTEGER),
                                    "name": openapi.Schema(type=openapi.TYPE_STRING),
                                },
                            ),
                        ),
                    },
                ),
            )
        }
    )
    def get(self, request):
        data = {
            "color": Color.objects.all(),
            "size": Size.objects.all(),
            "compound": Compound.objects.all(),
        }
        serializer = MenuSerializer(instance=data, context={"request": request})
        return Response(serializer.data)

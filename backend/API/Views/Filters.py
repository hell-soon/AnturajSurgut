from rest_framework.response import Response
from rest_framework.views import APIView

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from DB.models import Color, Size, Compound
from API.serializers.MenuSerializers import MenuSerializer
from API.Utils.Prices.MinMaxPrice import calculated_range_cost


class FilterMenu(APIView):
    @swagger_auto_schema(
        responses={
            200: MenuSerializer(many=True),
        }
    )
    def get(self, request):
        filter_menu_data = {
            "color": Color.objects.all(),
            "size": Size.objects.all(),
            "compound": Compound.objects.all(),
            "cost_range": calculated_range_cost(),
        }
        serializer = MenuSerializer(instance=filter_menu_data)
        return Response(serializer.data)

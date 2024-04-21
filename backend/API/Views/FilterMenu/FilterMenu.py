from rest_framework.response import Response
from rest_framework.views import APIView
from DB.models import Color, Size, Compound
from API.serializers.MenuSerializers import MenuSerializer


class FilterMenu(APIView):
    def get(self, request):
        data = {
            "color": Color.objects.all(),
            "size": Size.objects.all(),
            "compound": Compound.objects.all(),
        }
        serializer = MenuSerializer(instance=data, context={"request": request})
        return Response(serializer.data)

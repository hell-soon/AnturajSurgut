from DB.models import Color


class ColorCreator:
    def create(self):
        colors = [
            Color(name="красный", color="#FF0000"),
            Color(name="оранжевый", color="#FFA500"),
            Color(name="желтый", color="#FFFF00"),
            Color(name="зеленый", color="#008000"),
            Color(name="голубой", color="#00FFFF"),
            Color(name="синий", color="#0000FF"),
            Color(name="фиолетовый", color="#800080"),
            Color(name="черный", color="#000000"),
            Color(name="белый", color="#FFFFFF"),
            Color(name="серый", color="#808080"),
            Color(name="бордовый", color="#A52A2A"),
            Color(name="коричневый", color="#A52A2A"),
            Color(name="серебристый", color="#C0C0C0"),
            Color(name="темно-серый", color="#696969"),
            Color(name="темно-коричневый", color="#8B4513"),
            Color(name="темно-бордовый", color="#8B0000"),
            Color(name="темно-фиолетовый", color="#4B0082"),
            Color(name="темно-синий", color="#000080"),
            Color(name="темно-зеленый", color="#006400"),
            Color(name="темно-голубой", color="#008B8B"),
            Color(name="темно-серый", color="#A9A9A9"),
            Color(name="светло-серый", color="#D3D3D3"),
            Color(name="светло-коричневый", color="#D2691E"),
            Color(name="светло-бордовый", color="#FFDAB9"),
            Color(name="светло-фиолетовый", color="#E6E6FA"),
            Color(name="светло-синий", color="#ADD8E6"),
            Color(name="светло-зеленый", color="#90EE90"),
            Color(name="светло-голубой", color="#B0E0E6"),
            Color(name="светло-жёлтый", color="#FFFFE0"),
            Color(name="светло-оранжевый", color="#FFA07A"),
        ]
        Color.objects.bulk_create(colors)
        return colors

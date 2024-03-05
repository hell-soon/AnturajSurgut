from DB.models import Color


class ColorCreator:
    def create(self):
        colors = [
            Color(name="красный", code="#FF0000"),
            Color(name="оранжевый", code="#FFA500"),
            Color(name="желтый", code="#FFFF00"),
            Color(name="зеленый", code="#008000"),
            Color(name="голубой", code="#00FFFF"),
            Color(name="синий", code="#0000FF"),
            Color(name="фиолетовый", code="#800080"),
            Color(name="черный", code="#000000"),
            Color(name="белый", code="#FFFFFF"),
            Color(name="серый", code="#808080"),
            Color(name="бордовый", code="#A52A2A"),
            Color(name="коричневый", code="#A52A2A"),
            Color(name="серебристый", code="#C0C0C0"),
            Color(name="темно-серый", code="#696969"),
            Color(name="темно-коричневый", code="#8B4513"),
            Color(name="темно-бордовый", code="#8B0000"),
            Color(name="темно-фиолетовый", code="#4B0082"),
            Color(name="темно-синий", code="#000080"),
            Color(name="темно-зеленый", code="#006400"),
            Color(name="темно-голубой", code="#008B8B"),
            Color(name="темно-серый", code="#A9A9A9"),
            Color(name="светло-серый", code="#D3D3D3"),
            Color(name="светло-коричневый", code="#D2691E"),
            Color(name="светло-бордовый", code="#FFDAB9"),
            Color(name="светло-фиолетовый", code="#E6E6FA"),
            Color(name="светло-синий", code="#ADD8E6"),
            Color(name="светло-зеленый", code="#90EE90"),
            Color(name="светло-голубой", code="#B0E0E6"),
            Color(name="светло-жёлтый", code="#FFFFE0"),
            Color(name="светло-оранжевый", code="#FFA07A"),
        ]
        Color.objects.bulk_create(colors)
        return colors

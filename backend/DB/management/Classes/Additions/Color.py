from DB.models import Color


class ColorCreator:
    def create(self):
        colors = [
            Color(color="#FF0000"),
            Color(color="#FFA500"),
            Color(color="#FFFF00"),
            Color(color="#008000"),
            Color(color="#00FFFF"),
            Color(color="#0000FF"),
            Color(color="#800080"),
            Color(color="#000000"),
            Color(color="#FFFFFF"),
            Color(color="#808080"),
            Color(color="#A52A2A"),
            Color(color="#A52A2A"),
            Color(color="#C0C0C0"),
            Color(color="#696969"),
            Color(color="#8B4513"),
            Color(color="#8B0000"),
            Color(color="#4B0082"),
            Color(color="#000080"),
            Color(color="#006400"),
            Color(color="#008B8B"),
            Color(color="#A9A9A9"),
            Color(color="#D3D3D3"),
            Color(color="#D2691E"),
            Color(color="#FFDAB9"),
            Color(color="#E6E6FA"),
            Color(color="#ADD8E6"),
            Color(color="#90EE90"),
            Color(color="#B0E0E6"),
            Color(color="#FFFFE0"),
            Color(color="#FFA07A"),
        ]
        Color.objects.bulk_create(colors)
        return colors

import os
from sitedb.models import Slider
from django.core.files import File
from pathlib import Path


class SliderCreator:
    def create(self):
        sliders = []
        for i in range(1, 6):
            slider = Slider(
                title=f"Test Slider {i}",
                text="Test text",
                is_active=True,
            )
            image_path = os.path.join("media", "TestDataImage", f"{i}.jpg")
            with open(image_path, "rb") as image_file:
                slider.image.save(f"test_image{i}.jpg", File(image_file), save=True)
            sliders.append(slider)
        Slider.objects.bulk_create(sliders)

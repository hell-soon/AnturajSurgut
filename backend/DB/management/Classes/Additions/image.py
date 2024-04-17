from DB.models import ProductImage
from django.core.files import File
import os


class ProductImageCreator:
    def __init__(self, dir):
        self.dir = dir

    def create(self):
        for filename in os.listdir(self.dir):
            file_path = os.path.join(self.dir, filename)
            if os.path.isfile(file_path):
                with open(file_path, "rb") as file:
                    product_image = ProductImage(image=File(file))
                    product_image.save()

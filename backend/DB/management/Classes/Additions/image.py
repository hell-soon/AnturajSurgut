from DB.models import ProductImage
from django.core.files import File


class ProductImageCreator:
    def __init__(self, image_dir):
        self.image_dir = image_dir

    def create(self, image_files):
        for image_file in image_files:
            # Создаем объект картинки
            product_image = ProductImage()

            # Открываем файл и загружаем его в модель
            with open(f"{self.image_dir}/{image_file}", "rb") as f:
                product_image.image.save(image_file, File(f))

            # Сохраняем модель в базе данных
            product_image.save()

import os
from django.db import models
from colorfield.fields import ColorField
from django_ckeditor_5.fields import CKEditor5Field


class Catalog(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название каталога")
    image = models.ImageField(
        upload_to="catalog_images/", verbose_name="Картинка", blank=True, null=True
    )
    id_1C = models.CharField(
        max_length=255, verbose_name="ID 1C", blank=True, null=True
    )
    verbose_name = "Каталог"
    verbose_name_plural = "Каталоги"

    class Meta:
        verbose_name = "Каталог"
        verbose_name_plural = "Каталоги"

    def delete(self, *args, **kwargs):
        if os.path.isfile(self.image.path):
            os.remove(self.image.path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.name


class SubCatalog(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название подкаталога")
    image = models.ImageField(
        upload_to="subcatalog_images/",
        blank=True,
        null=True,
        verbose_name="Загрузить картинку",
    )
    catalog = models.ForeignKey(
        Catalog, on_delete=models.CASCADE, verbose_name="Каталог", blank=True, null=True
    )
    id_1C = models.CharField(
        max_length=255, verbose_name="ID 1C", blank=True, null=True
    )
    verbose_name = "Подкаталог"
    verbose_name_plural = "Подкаталоги"

    def delete(self, *args, **kwargs):
        if os.path.isfile(self.image.path):
            os.remove(self.image.path)
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = "Подкаталог"
        verbose_name_plural = "Подкаталоги"

    def __str__(self):
        return self.name


class Tags(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название тэга")
    id_1C = models.CharField(
        max_length=255, verbose_name="ID 1C", blank=True, null=True
    )
    verbose_name = "Тэг"
    verbose_name_plural = "Тэги"

    class Meta:
        verbose_name = "Тэг"
        verbose_name_plural = "Тэги"

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    image = models.ImageField(
        upload_to="product_images/", verbose_name="Загрузить картинку"
    )
    verbose_name = "Изображение"
    verbose_name_plural = "Изображения"

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"

    def delete(self, *args, **kwargs):
        if os.path.isfile(self.image.path):
            os.remove(self.image.path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.image.url


class Color(models.Model):
    name = models.CharField(max_length=20, verbose_name="Название")
    color = ColorField(default="#FFFFFF", verbose_name="Код")

    class Meta:
        verbose_name = "Цвет"
        verbose_name_plural = "Цвета"

    def __str__(self):
        return self.name


class Size(models.Model):
    name = models.CharField(max_length=20, verbose_name="Размер")
    verbose_name = "Размер"
    verbose_name_plural = "Размеры"

    class Meta:
        verbose_name = "Размер"
        verbose_name_plural = "Размеры"

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=20, verbose_name="Тип")
    verbose_name = "Тип"
    verbose_name_plural = "Типы"

    class Meta:
        verbose_name = "Тип"
        verbose_name_plural = "Типы"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    description = CKEditor5Field("Описание", config_name="extends")
    image = models.ManyToManyField(ProductImage, verbose_name="Изображение", blank=True)
    sub_catalog = models.ForeignKey(
        SubCatalog, on_delete=models.CASCADE, verbose_name="Подкаталог"
    )
    tags = models.ManyToManyField(
        Tags, verbose_name="Тэги", blank=True, help_text="Тэги"
    )
    product_status = models.BooleanField(default=True, verbose_name="Активен")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    rating = models.IntegerField(
        default=0,
        verbose_name="Рейтинг",
        help_text="Рейтинг товара, заполняется автоматически",
    )

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name


class ProductInfo(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Товар")
    color = models.ForeignKey(
        Color, on_delete=models.CASCADE, verbose_name="Цвет", blank=True, null=True
    )
    size = models.ForeignKey(
        Size, on_delete=models.CASCADE, verbose_name="Размер", blank=True, null=True
    )
    quantity = models.IntegerField(default=0, verbose_name="Количество")
    cost = models.FloatField(null=True, blank=True, verbose_name="Цена")
    promotion = models.BooleanField(default=False, verbose_name="Товар по акции")
    promotion_cost = models.FloatField(
        null=True, blank=True, verbose_name="Цена с учетом акции"
    )
    unique_together = ("product", "color", "size")

    class Meta:
        verbose_name = "Информация о продукте"
        verbose_name_plural = "Линейка товара"

    def __str__(self):
        return f"{self.product.name} {self.color} {self.size}"

from django.db import models

# Create your models here.


class Catalog(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название каталога")
    image = models.ImageField(
        upload_to="catalog_images/", verbose_name="Картинка", blank=True, null=True
    )
    verbose_name = "Каталог"
    verbose_name_plural = "Каталоги"

    class Meta:
        verbose_name = "Каталог"
        verbose_name_plural = "Каталоги"

    def __str__(self):
        return self.name


class SubCatalog(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название подкаталога")
    image = models.ImageField(upload_to="subcatalog_images/", blank=True, null=True)
    catalog = models.ForeignKey(
        Catalog, on_delete=models.CASCADE, verbose_name="Каталог", blank=True, null=True
    )
    verbose_name = "Подкаталог"
    verbose_name_plural = "Подкаталоги"

    class Meta:
        verbose_name = "Подкаталог"
        verbose_name_plural = "Подкаталоги"

    def __str__(self):
        return self.name


class Tags(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название тэга")
    verbose_name = "Тэг"
    verbose_name_plural = "Тэги"

    class Meta:
        verbose_name = "Тэг"
        verbose_name_plural = "Тэги"

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    image = models.ImageField(
        upload_to="product_images/", verbose_name="Картинки товаров"
    )
    verbose_name = "Изображение"
    verbose_name_plural = "Изображения"

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"

    def __str__(self):
        return self.image.url


class Color(models.Model):
    name = models.CharField(max_length=20, verbose_name="Цвет")
    code = models.CharField(max_length=20, verbose_name="Код цвета")
    verbose_name = "Цвет"
    verbose_name_plural = "Цвета"

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
    description = models.TextField(blank=True, verbose_name="Описание")
    image = models.ManyToManyField(ProductImage, verbose_name="Изображение")
    sub_catalog = models.ForeignKey(
        SubCatalog,
        on_delete=models.CASCADE,
        verbose_name="Подкаталог",
        blank=True,
        null=True,
    )
    tags = models.ManyToManyField(Tags, verbose_name="Тэги", blank=True)
    product_status = models.BooleanField(default=True, verbose_name="Активен")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    rating = models.IntegerField(default=0, verbose_name="Рейтинг")

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name


class ProductInfo(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Товар")
    color = models.ForeignKey(Color, on_delete=models.CASCADE, verbose_name="Цвет")
    size = models.ForeignKey(Size, on_delete=models.CASCADE, verbose_name="Размер")
    quantity = models.IntegerField(default=0, verbose_name="Количество")
    cost = models.FloatField(null=True, blank=True, verbose_name="Цена")
    promotion = models.BooleanField(default=False, verbose_name="Товар по акции")
    promotion_cost = models.FloatField(
        null=True, blank=True, verbose_name="Цена с учетом акции"
    )
    unique_together = ("product", "color", "size")

    class Meta:
        verbose_name = "Информация о продукте"
        verbose_name_plural = "Информация о продуктах"

    def __str__(self):
        return f"{self.product.name} - {self.id}"
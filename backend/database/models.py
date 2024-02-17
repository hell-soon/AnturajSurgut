from django.db import models
from users.models import CustomUser
from django.db.models import UniqueConstraint
from .utils.order_number_generator import generate_order_number


class Catalog(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название каталога")
    image = models.ImageField(
        upload_to="catalog_images/", verbose_name="Картинка", blank=True, null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Каталог"
        verbose_name_plural = "Каталоги"


class SubCatalog(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название подкаталога")
    image = models.ImageField(upload_to="subcatalog_images", blank=True, null=True)
    catalog = models.ForeignKey(
        Catalog, on_delete=models.CASCADE, verbose_name="Каталог", blank=True, null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Подкаталог"
        verbose_name_plural = "Подкаталоги"


class Size(models.Model):
    name = models.CharField(max_length=20, verbose_name="Размер")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Размер"
        verbose_name_plural = "Размеры"


class ProductImage(models.Model):
    image = models.ImageField(
        upload_to="product_images", verbose_name="Картинки товаров"
    )

    def __str__(self):
        return self.image.url

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"


class Tags(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название тэга")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тэг"
        verbose_name_plural = "Тэги"


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название товара")
    cost = models.FloatField(verbose_name="Цена")
    count = models.IntegerField(verbose_name="На складе", default=0)
    rating = models.IntegerField(default=0, verbose_name="Рейтинг")
    description = models.TextField(blank=True, verbose_name="Описание")
    size = models.ManyToManyField(Size, verbose_name="Размеры")
    subcatalog = models.ForeignKey(
        SubCatalog, on_delete=models.DO_NOTHING, verbose_name="Категория"
    )
    image = models.ManyToManyField(ProductImage, verbose_name="Изображение", blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    promotion = models.BooleanField(default=False, verbose_name="Товар по акции")
    promotion_cost = models.FloatField(
        null=True, blank=True, verbose_name="Цена с учетом акции"
    )
    tags = models.ManyToManyField(Tags, verbose_name="Тэги")

    def sell(self):
        self.count -= 1
        self.rating += 1
        self.save()

    def save(self, *args, **kwargs):
        if self.promotion and not self.promotion_cost:
            self.promotion_cost = self.cost
        super().save(
            *args,
            **kwargs,
        )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class Order(models.Model):
    CHOICES_TYPES = (
        ("1", "Самовывоз"),
        ("2", "Доставка до двери"),
        ("3", "Доставка транспортной компанией"),
    )

    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, verbose_name="Заказчик"
    )
    products = models.JSONField(verbose_name="Товары")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Сформирован")
    order_number = models.CharField(
        max_length=10,
        verbose_name="Номер заказа",
        unique=True,
        default=generate_order_number,
    )
    order_type = models.CharField(
        max_length=1, choices=CHOICES_TYPES, default="1", verbose_name="Тип доставки"
    )
    order_status = models.BooleanField(default=False, verbose_name="Статус оплаты")
    order_address = models.CharField(
        max_length=255, verbose_name="Адрес доставки", blank=True
    )

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def save(self, *args, **kwargs):
        if self.order_type == "1":
            self.order_address = "Самовывоз"
        super(Order, self).save(*args, **kwargs)

    def __str__(self):
        return (
            f"Заказ от {self.created_at} - {self.user.first_name} {self.user.last_name}"
        )

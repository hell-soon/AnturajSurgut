from django.db import models
from DB.models import ProductInfo
from DB.utils.order_number_generator import generate_order_number
from django.db.models import Q
from users.models import CustomUser
from icecream import ic


class Additionalservices(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название доп.услуги")
    cost = models.FloatField(verbose_name="Цена")

    class Meta:
        verbose_name = "Доп.услуга"
        verbose_name_plural = "Доп.услуги"

    def __str__(self):
        return self.name


class Order(models.Model):
    CHOICES_TYPES = (
        ("1", "Самовывоз"),
        ("2", "Доставка до двери"),
        ("3", "Доставка транспортной компанией"),
    )
    CHOICES_FACE = (
        ("1", "Юридическое лицо"),
        ("2", "Физическое лицо"),
    )
    CHOICES_STATUS = (
        ("1", "Не готов"),
        ("2", "Готов к выдаче"),
        ("3", "Передан в доставку"),
        ("4", "Доставлен"),
        ("5", "Отменен"),
        ("6", "Завершен"),
    )
    PAYMENT_STATUS = (
        ("1", "Онланй платеж"),
        ("2", "При получении"),
    )
    user_initials = models.CharField(max_length=100, verbose_name="Инициалы покупателя")
    user_email = models.EmailField(
        verbose_name="Электронная почта", blank=True, null=True
    )
    user_phone = models.CharField(
        max_length=20, verbose_name="Номер телефона", blank=True, null=True
    )
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
    payment_type = models.CharField(
        max_length=1, choices=PAYMENT_STATUS, default="1", verbose_name="Способ оплаты"
    )
    order_paymant = models.BooleanField(default=False, verbose_name="Оплачен")
    order_address = models.CharField(
        max_length=255, verbose_name="Адрес доставки", blank=True
    )
    order_face = models.CharField(
        max_length=1, choices=CHOICES_FACE, default="1", verbose_name="Тип лица"
    )
    order_status = models.CharField(
        max_length=1, choices=CHOICES_STATUS, default="1", verbose_name="Статус"
    )
    order_additionalservices = models.ManyToManyField(
        Additionalservices, verbose_name="Доп.услуги", blank=True
    )
    track_number = models.CharField(
        max_length=255, verbose_name="Номер отслеживания", blank=True
    )
    comment = models.TextField(verbose_name="Комментарии", blank=True)
    user_register = models.BooleanField(default=False, verbose_name="Зарегистрирован")

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def save(self, *args, **kwargs):
        if self.order_type == "1":
            self.order_address = "Самовывоз"
            self.track_number = "Самовывоз"

        try:
            user = CustomUser.objects.get(
                Q(email=self.user_email) | Q(phone=self.user_phone)
            )
            self.user_email = user.email
            self.user_phone = user.phone
            self.user_initials = f"{user.first_name} {user.last_name}"
            self.user_register = True
        except CustomUser.DoesNotExist:
            pass

        if not self.user_phone:
            self.user_phone = "Телефон не указан"
        super(Order, self).save(*args, **kwargs)

    def __str__(self):
        return f"Заказ от {self.created_at.strftime('%d.%m.%Y %H:%M')} - {self.user_initials}"


class OrderItems(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, verbose_name="номер заказа"
    )
    product = models.ForeignKey(
        ProductInfo, on_delete=models.CASCADE, verbose_name="Товар"
    )
    color = models.CharField(max_length=100, verbose_name="Цвет", blank=True, null=True)
    size = models.CharField(
        max_length=100, verbose_name="Размер", blank=True, null=True
    )
    cost = models.FloatField(verbose_name="Цена", blank=True, null=True)
    quantity = models.PositiveIntegerField(verbose_name="Количество")
    total_cost = models.FloatField(verbose_name="Общая цена", blank=True, null=True)

    class Meta:
        verbose_name = "Детали заказа"
        verbose_name_plural = "Детали заказа"

    def save(self, *args, **kwargs):
        if self.pk is None:  # Проверяем, что это новый объект
            if self.product.promotion:
                self.cost = self.product.promotion_cost
                self.total_cost = self.product.promotion_cost * self.quantity
            else:
                self.cost = self.product.cost
                self.total_cost = self.cost * self.quantity
            self.color = self.product.color.name
            self.size = self.product.size.name

            # Списание товара со склада
            product_info = self.product
            product_info.quantity -= self.quantity
            product_info.save()

        super(OrderItems, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.order.order_number} - {self.product}"

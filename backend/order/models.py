from django.db import models
from DB.models import ProductInfo
from DB.utils.order_number_generator import generate_order_number
from django.db.models import Q
from users.models import CustomUser
from icecream import ic
from sitedb.models import Sertificate

from django.core.exceptions import ValidationError
from .misc.upd_info import quantity_check


class Additionalservices(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название доп.услуги")
    cost = models.FloatField(verbose_name="Цена")

    class Meta:
        verbose_name = "Доп.услуга"
        verbose_name_plural = "Доп.услуги"

    def __str__(self):
        return f"{self.name} - {self.cost} рублей"


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
    sertificate = models.ForeignKey(
        Sertificate,
        verbose_name="Сертификат",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def clean(self):
        # Проверяем, что сертификат действителен
        if self.sertificate:
            try:
                self.sertificate.use_sertificate()
            except ValidationError as e:
                raise ValidationError({"sertificate": e.message})

        if self.user_phone:
            if not self.user_phone.isdigit():
                raise ValidationError("Номер телефона должен содержать только цифры.")
            if len(self.user_phone) != 11:
                raise ValidationError(
                    "Номер телефона должен содержать минимум 11 цифр."
                )
        if not self.user_email and not self.user_phone:
            raise ValidationError(
                "Необходимо заполнить хотя бы одно из полей Электронная почта или Номер телефона"
            )

    def save(self, *args, **kwargs):

        if self.order_type == "1":
            self.order_address = "Самовывоз"
            self.track_number = "Самовывоз"
        self.full_clean()
        super(Order, self).save(*args, **kwargs)

    def total_cost(self):
        # Инициализируем общую стоимость заказа
        total = 0

        # Суммируем стоимость товаров
        for item in self.orderitems_set.all():
            total += item.cost * item.quantity

        # Суммируем стоимость дополнительных услуг
        for service in self.order_additionalservices.all():
            total += service.cost

        # Если есть сертификат, применяем скидку
        if self.sertificate:
            total -= total * (self.sertificate.discount / 100)

        return round(total, 2)

    def __str__(self):
        return f"Заказ: {self.order_number}"


from icecream import ic


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
    cost = models.FloatField(verbose_name="Цена за шт", blank=True, null=True)
    quantity = models.PositiveIntegerField(verbose_name="Количество")
    total_cost = models.FloatField(verbose_name="Общая цена", blank=True, null=True)

    class Meta:
        verbose_name = "Детали заказа"
        verbose_name_plural = "Детали заказа"

    def clean(self):
        if self.product.quantity < self.quantity:
            raise ValidationError(
                f"Количество {self.product.product.name} превышает количество на складе. В наличии {self.product.quantity}"
            )

    def save(self, *args, **kwargs):
        """
        Сохранение объекта, проверяеться акционный ли продукт и высчитаываеться общая цена лота в заказе(с учетом акции), Можно добавить Вычет НДС и тд
        total_cost - общая цена лота
        cost - цена товара за 1 шт
        quantity - кол-во единиц в лоте
        """
        if self.pk is None:  # Проверяем, что это новый объект
            # Товар акционный?
            if self.product.promotion:
                self.cost = self.product.promotion_cost
                self.total_cost = self.product.promotion_cost * self.quantity
            else:
                # Товар без акции
                self.cost = self.product.cost
                self.total_cost = self.cost * self.quantity
            self.color = self.product.color.name
            self.size = self.product.size.name

            # Списание товара со склада
            product_info = self.product
            product_info.quantity -= self.quantity
            product_info.save()

        if self.pk:
            original_obj = OrderItems.objects.get(pk=self.pk)
            if original_obj.quantity != self.quantity:
                quantity_check(
                    original_obj.quantity,
                    self.quantity,
                    ProductInfo.objects.get(pk=self.product.pk),
                )
                product = ProductInfo.objects.get(pk=self.product.pk)
                if product.promotion:
                    self.cost = self.product.promotion_cost
                    self.total_cost = self.product.promotion_cost * self.quantity
                else:
                    self.cost = self.product.cost
                    self.total_cost = round(self.cost * self.quantity, 2)
        super(OrderItems, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.order.order_number} - {self.product}"

from django.db import models
from DB.models import ProductInfo

from sitedb.models import Sertificate

from django.core.exceptions import ValidationError
from .misc.upd_info import quantity_check
from .misc.code_generator import generate_order_number


class OrderSettings(models.Model):
    name = models.CharField(max_length=255, verbose_name="Наименование")

    class Meta:
        verbose_name = "Настройка"
        verbose_name_plural = "Настройки"

    def __str__(self):
        return self.name


class Additionalservices(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название доп.услуги")
    cost = models.FloatField(verbose_name="Цена")

    class Meta:
        verbose_name = "Доп.услуга"
        verbose_name_plural = "Доп.услуги"

    def __str__(self):
        return f"{self.name} - {self.cost} рублей"


class OrderType(models.Model):
    settings = models.ForeignKey(OrderSettings, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name="Тип")

    class Meta:
        verbose_name = "Тип заказа"
        verbose_name_plural = "Типы заказов"

    def __str__(self):
        return self.name


class OrderFace(models.Model):
    settings = models.ForeignKey(OrderSettings, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name="Название")

    class Meta:
        verbose_name = "Тип заказчика"
        verbose_name_plural = "Типы заказчиков"

    def __str__(self):
        return self.name


class PaymentType(models.Model):
    settings = models.ForeignKey(OrderSettings, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name="Название")

    class Meta:
        verbose_name = "Тип оплаты"
        verbose_name_plural = "Типы оплаты"

    def __str__(self):
        return self.name


class OrderStatus(models.Model):
    settings = models.ForeignKey(OrderSettings, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name="Название")

    class Meta:
        verbose_name = "Статус заказа"
        verbose_name_plural = "Статусы заказов"

    def __str__(self):
        return self.name


class Order(models.Model):
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
    order_type = models.ForeignKey(
        OrderType,
        verbose_name="Тип доставки",
        on_delete=models.CASCADE,
        help_text="""При выборе "Самовывоз" адрес заполняется автоматически""",
    )
    payment_type = models.ForeignKey(
        PaymentType, verbose_name="Способ оплаты", on_delete=models.CASCADE
    )
    order_paymant = models.BooleanField(default=False, verbose_name="Оплачен")
    order_face = models.ForeignKey(
        OrderFace, verbose_name="Тип лица", on_delete=models.CASCADE
    )
    order_status = models.ForeignKey(
        OrderStatus, verbose_name="Статус", on_delete=models.CASCADE, default=1
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
    payment_id = models.CharField(
        max_length=255, verbose_name="ID платежа в Юкассе", blank=True
    )
    # user = models.ForeignKey(
    #     CustomUser, on_delete=models.CASCADE, verbose_name="Пользователь", blank=True
    # )

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def clean(self):
        errors = {}

        # Проверяем, что сертификат действителен
        if self.sertificate:
            try:
                self.sertificate.use_sertificate()
            except ValidationError as e:
                errors["sertificate"] = e.message

        # Проверяем номер телефона
        if self.user_phone:
            if not self.user_phone.isdigit():
                errors["user_phone"] = "Номер телефона должен содержать только цифры."
            if len(self.user_phone) != 11:
                errors["user_phone"] = "Номер телефона должен содержать 11 цифр."

        # Проверяем, что заполнено хотя бы одно из полей
        if not self.user_email and not self.user_phone:
            errors["__all__"] = (
                "Необходимо заполнить хотя бы одно из полей Электронная почта или Номер телефона"
            )

        if errors:
            raise ValidationError(errors)

    def save(self, *args, **kwargs):
        self.full_clean()

        super(Order, self).save(*args, **kwargs)

    def total_cost(self):
        total = 0

        total += sum(item.cost * item.quantity for item in self.orderitems_set.all())

        total += sum(service.cost for service in self.order_additionalservices.all())

        if self.sertificate:
            total -= total * (self.sertificate.discount / 100)

        return round(total, 2)

    def __str__(self):
        return f"Заказ: {self.order_number}"


class OrderItems(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, verbose_name="номер заказа"
    )
    product = models.ForeignKey(
        ProductInfo,
        related_name="order_items",
        on_delete=models.CASCADE,
        verbose_name="Товар",
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
        if self.product_id is None:  # Проверяем, что товар выбран
            raise ValidationError("Выберите товар")
        else:
            try:
                if self.product.quantity < self.quantity:
                    raise ValidationError(
                        f"Количество {self.product.product.name} превышает количество на складе. В наличии {self.product.quantity}"
                    )
            except ProductInfo.DoesNotExist:
                raise ValidationError("Товар не найден")

    def calculate_price(self):
        if self.product.promotion:
            self.cost = self.product.promotion_cost
            self.total_cost = round(self.product.promotion_cost * self.quantity, 2)
        else:
            self.cost = self.product.cost
            self.total_cost = round(self.cost * self.quantity, 2)

    def save(self, *args, **kwargs):
        if self.pk is None:  # Проверяем, что это новый объект
            self.calculate_price()
            self.color = self.product.color.name
            self.size = self.product.size.name

            # Списание товара со склада
            self.product.quantity -= self.quantity
            self.product.save(update_fields=["quantity"])

        if self.pk:
            original_obj = OrderItems.objects.get(pk=self.pk)
            if original_obj.quantity != self.quantity:
                quantity_check(
                    original_obj.quantity,
                    self.quantity,
                    ProductInfo.objects.get(pk=self.product.pk),
                )
                self.calculate_price()
        super(OrderItems, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.product}"


class OrderAddress(models.Model):
    order = models.ForeignKey(
        Order,
        related_name="items",
        on_delete=models.CASCADE,
        verbose_name="номер заказа",
    )
    city = models.CharField(max_length=100, verbose_name="Город")
    region = models.CharField(max_length=100, verbose_name="Область", blank=True)
    street = models.CharField(max_length=100, verbose_name="Улица")
    house = models.CharField(max_length=10, verbose_name="Дом")
    apartment = models.CharField(max_length=10, verbose_name="Квартира", blank=True)
    floor = models.IntegerField(verbose_name="Этаж", blank=True, null=True)
    post_index = models.CharField(
        max_length=6, verbose_name="Почтовый индекс", blank=True
    )

    class Meta:
        verbose_name = "Адрес"
        verbose_name_plural = "Адрес"

    def __str__(self):
        return f"{self.region}, {self.city}, {self.street}, {self.house}, {self.apartment}, {self.floor}, Почтовый индекс: {self.post_index}"


class LegalDate(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, verbose_name="номер заказа"
    )
    name = models.CharField(max_length=255, verbose_name="Название Юр. лица")
    inn = models.CharField(max_length=255, verbose_name="ИНН")
    ogrn = models.CharField(max_length=255, verbose_name="ОГРН/ЕГРП")
    kpp = models.CharField(max_length=255, verbose_name="КПП")
    bik = models.CharField(max_length=255, verbose_name="БИК")
    bank_name = models.CharField(max_length=255, verbose_name="Название банка")
    cores_account = models.CharField(
        max_length=255, verbose_name="Корреспондентский счет", blank=True
    )
    ras_check = models.CharField(
        max_length=255, verbose_name="Расчётный счет", blank=True
    )
    legal_address = models.CharField(
        max_length=255, verbose_name="Юридический адрес", blank=True
    )

    class Meta:
        verbose_name = "Юридические данные"
        verbose_name_plural = "Юридические данные"

    def __str__(self):
        return f"{self.order}"

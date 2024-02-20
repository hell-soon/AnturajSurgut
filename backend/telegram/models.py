from django.db import models

# Create your models here.


class TelegramImage(models.Model):
    image = models.ImageField(upload_to="telegram_images/")

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"

    def __str__(self):
        return self.image.url


class TelegramNews(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ManyToManyField(TelegramImage, blank=True)

    class Meta:
        verbose_name = "Новость в телеграмме"
        verbose_name_plural = "Новости в телеграмме"

    def __str__(self):
        return self.title


class TelegramImageOrder(models.Model):
    CHOICE_STATUS = (
        ("1", "Не готов"),
        ("2", "Готов к выдаче"),
        ("3", "Передан в доставку"),
        ("4", "Доставлен"),
        ("5", "Отменен"),
        ("6", "Завершен"),
    )
    order_status = models.CharField(
        max_length=1, choices=CHOICE_STATUS, unique=True, verbose_name="Статус заказа"
    )
    image = models.ImageField(upload_to="telegram_images_orders/")

    class Meta:
        verbose_name = "Изображение для отображения в заказе"
        verbose_name_plural = "Изображения для отображения в заказе"

    def __str__(self):
        return self.image.url

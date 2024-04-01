from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from .Utils.Code.Sertificate.sertificate_generator import generate_certificate
from django.core.exceptions import ValidationError
from django.utils import timezone
from django_ckeditor_5.fields import CKEditor5Field


class Slider(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    text = CKEditor5Field("Текст", config_name="extends")
    image = models.ImageField(upload_to="slider/", verbose_name="Картинка")
    is_active = models.BooleanField(default=True, verbose_name="Активен")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Слайдер"
        verbose_name_plural = "Слайдер"


class Service(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    image = models.ImageField(upload_to="service/", verbose_name="Картинка")
    url = models.URLField(blank=True, null=True, verbose_name="Ссылка")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    text = models.TextField(verbose_name="Текст")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    image = models.ImageField(upload_to="news/", verbose_name="Картинка")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


class OurWorkImage(models.Model):
    image = models.ImageField(upload_to="our_work/", verbose_name="Картинка")

    def __str__(self):
        return self.image.url

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"


class OurWork(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    work_list = models.TextField(verbose_name="Перечень работ")
    description = models.TextField(verbose_name="Описание")
    image = models.ManyToManyField(OurWorkImage, verbose_name="Картинки нашей работы")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Наши работы"
        verbose_name_plural = "Наши работы"


class Sertificate(models.Model):
    code = models.CharField(
        default=generate_certificate,
        verbose_name="Код",
        unique=True,
        max_length=20,
    )
    quanity = models.IntegerField(default=0, verbose_name="Количество использованний")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    end_date = models.DateTimeField(verbose_name="Дата окончания")
    status = models.BooleanField(default=True, verbose_name="Статус")
    personal = models.BooleanField(
        default=False,
        verbose_name="Персональный",
        help_text="Сертификат не будет отправлен всем пользователям, которые подписались на рассылку",
    )
    discount = models.IntegerField(
        default=10,
        verbose_name="Скидка",
        validators=[MaxValueValidator(100), MinValueValidator(0)],
        help_text="Размер скидки в процентах",
    )

    class Meta:
        verbose_name = "Сертификат"
        verbose_name_plural = "Сертификаты"

    def use_sertificate(self):
        if self.status and self.quanity > 0 and self.end_date > timezone.now():
            self.quanity -= 1
            self.save()
        else:
            pass

    def __str__(self):
        return self.code

import os
from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
from django.utils import timezone
from django_ckeditor_5.fields import CKEditor5Field

from .Utils.Code.Sertificate.sertificate_generator import generate_certificate


class SiteImage(models.Model):
    image = models.ImageField(upload_to="site/", verbose_name="Картинка")

    def __str__(self):
        return os.path.basename(self.image.name)

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"


class OurWorkImage(models.Model):
    image = models.ImageField(upload_to="site/", verbose_name="Картинка")

    def __str__(self):
        return os.path.basename(self.image.name)

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"


class Slider(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    text = CKEditor5Field("Текст", config_name="extends")
    url = models.URLField(max_length=255, verbose_name="Ссылка")
    image = models.ImageField(upload_to="slider/", verbose_name="Картинка")
    is_active = models.BooleanField(default=True, verbose_name="Активен")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Слайдер"
        verbose_name_plural = "Слайдер"


class OurWork(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    work_list = models.TextField(verbose_name="Перечень работ")
    description = models.TextField(verbose_name="Описание")
    image = models.ManyToManyField(SiteImage, verbose_name="Картинки нашей работы")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Наши работы"
        verbose_name_plural = "Наши работы"


class Service(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    text = CKEditor5Field(
        "Текст",
        config_name="extends",
        help_text="Текст который будет отображен на странице",
    )
    is_active = models.BooleanField(default=True, verbose_name="Активен")
    image = models.ImageField(upload_to="service/", verbose_name="Картинка", blank=True)
    our_work_is_active = models.BooleanField(
        default=False, verbose_name="Отоброжать наши работы"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"


class ServiceSlider(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    site_image = models.ForeignKey(
        SiteImage,
        on_delete=models.CASCADE,
        verbose_name="Картинки для слайдера",
        blank=True,
    )

    class Meta:
        verbose_name = "Слайдер"
        verbose_name_plural = "Слайдеры"


class ServiceOurWork(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    our_work = models.ForeignKey(
        OurWork, on_delete=models.CASCADE, blank=True, verbose_name="Наши работы"
    )

    class Meta:
        verbose_name = "Наша работа"
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


class SiteInfo(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")

    class Meta:
        verbose_name = "Информация о сайте"
        verbose_name_plural = "Информация о сайте"

    def __str__(self):
        return self.name


class Requisites(models.Model):
    info = models.ForeignKey(SiteInfo, on_delete=models.CASCADE)
    ip = models.CharField(max_length=255, verbose_name="ИП")
    inn = models.CharField(max_length=255, verbose_name="ИНН")
    legal_address = models.CharField(max_length=255, verbose_name="Юридический адрес")

    class Meta:
        verbose_name = "Реквизиты"
        verbose_name_plural = "Реквизиты"


class Contact(models.Model):
    info = models.ForeignKey(SiteInfo, on_delete=models.CASCADE)
    phone = models.CharField(max_length=255, verbose_name="Телефон")
    fax = models.CharField(max_length=255, verbose_name="Факс")
    email = models.EmailField(max_length=255, verbose_name="Email")

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"

    def __str__(self):
        return self.phone


class Address(models.Model):
    info = models.ForeignKey(SiteInfo, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, verbose_name="Адрес")
    longitude = models.CharField(max_length=100, verbose_name="Долгота")
    latitude = models.CharField(max_length=100, verbose_name="Широта")

    class Meta:
        verbose_name = "Адрес"
        verbose_name_plural = "Адреса"

    def __str__(self):
        return self.address


class WokrTime(models.Model):
    info = models.ForeignKey(SiteInfo, on_delete=models.CASCADE)
    work_time = models.CharField(max_length=255, verbose_name="Время работы")

    class Meta:
        verbose_name = "Время работы"
        verbose_name_plural = "Время работы"

    def __str__(self):
        return self.work_time


class SocialAccount(models.Model):
    info = models.ForeignKey(SiteInfo, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name="Название")
    url = models.CharField(max_length=255, verbose_name="Ссылка")
    icon = models.ImageField(upload_to="social/", verbose_name="Иконка")

    class Meta:
        verbose_name = "Социальная сеть"
        verbose_name_plural = "Социальные сети"

    def __str__(self):
        return self.name

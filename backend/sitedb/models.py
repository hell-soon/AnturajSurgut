import os
from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from .Utils.Code.Sertificate.sertificate_generator import generate_certificate
from django.core.exceptions import ValidationError
from django.utils import timezone
from django_ckeditor_5.fields import CKEditor5Field

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
    text = CKEditor5Field("Текст", config_name="extends", help_text="Текст который будет отображен в начале странице")
    table = CKEditor5Field("Таблица", config_name="extends", help_text="Текст который будет отображен внизу страницы")
    is_active = models.BooleanField(default=True, verbose_name="Активен")
    image = models.ImageField(upload_to="service/", verbose_name="Картинка", blank=True)
    slider = models.ManyToManyField(SiteImage, verbose_name="Слайдер", blank=True)
    our_work_is_active = models.BooleanField(default=True, verbose_name="Активен")
    our_work = models.ManyToManyField(OurWork, verbose_name="Наши работы", blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"


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


class Contact(models.Model):
    phone = models.CharField(max_length=255, verbose_name="Телефон")
    fax = models.CharField(max_length=255, verbose_name="Факс")
    email = models.EmailField(max_length=255, verbose_name="Email")

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"

    def __str__(self):
        return self.phone


class SocialAccount(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    url = models.CharField(max_length=255, verbose_name="Ссылка")
    icon = models.ImageField(upload_to="social/", verbose_name="Иконка")

    class Meta:
        verbose_name = "Социальная сеть"
        verbose_name_plural = "Социальные сети"

    def __str__(self):
        return self.name

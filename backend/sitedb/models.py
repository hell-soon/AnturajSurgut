from django.contrib.auth.models import User
from django.db import models

from users.models import CustomUser


class Slider(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    image = models.ImageField(upload_to="slider/", verbose_name="Картинка")
    url = models.URLField(blank=True, null=True, verbose_name="Ссылка")
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
        verbose_name = "Картинка нашей работы"
        verbose_name_plural = "Картинки нашей работы"


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

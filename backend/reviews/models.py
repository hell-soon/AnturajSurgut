from django.db import models
from users.models import CustomUser
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Review(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, verbose_name="Пользователь"
    )
    text = models.TextField(verbose_name="Текст")
    rating = models.PositiveIntegerField(
        verbose_name="Рейтинг", validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self):
        return f"Отзыв №{self.pk}"


class Feedback(models.Model):
    phone = models.CharField(max_length=255, verbose_name="Телефон")
    name = models.CharField(max_length=255, verbose_name="Имя")
    text = models.TextField(verbose_name="Текст", blank=True)
    is_active = models.BooleanField(default=False, verbose_name="Ответ предоствлен")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Фидбэк"
        verbose_name_plural = "Фидбэк"

    def __str__(self):
        return self.phone

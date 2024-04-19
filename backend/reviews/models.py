from django.db import models
from users.models import CustomUser
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Review(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(5)],
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"


class Feedback(models.Model):
    phone = models.CharField(max_length=255, verbose_name="Телефон")
    name = models.CharField(max_length=255, verbose_name="Имя")
    text = models.TextField(verbose_name="Текст", blank=True)
    is_active = models.BooleanField(default=False, verbose_name="Ответ предоствлен")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Фидбэк"
        verbose_name_plural = "Фидбэк"

    def __str__(self):
        return self.phone

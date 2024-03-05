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

from django.db import models


# Create your models here.
class Vacancy(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название вакансии")
    description = models.TextField(verbose_name="Описание вакансии")
    work_place = models.CharField(max_length=100, verbose_name="Место работы")
    work_time = models.CharField(max_length=100, verbose_name="График работы")
    is_active = models.BooleanField(default=True, verbose_name="Активна")
    salary = models.CharField(max_length=100, verbose_name="Зарплата")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.salary is None:
            self.salary = "Зарплата не указана"
        super(Vacancy, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Вакансию"
        verbose_name_plural = "Вакансии"


class ResponseVacancy(models.Model):
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    user = models.ForeignKey(
        "users.CustomUser",
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
    )
    name = models.CharField(max_length=100, verbose_name="Имя откликнувшегося")
    phone = models.CharField(max_length=100, verbose_name="Номер телефона")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"Отклик на вакансию {self.vacancy.name}"

    class Meta:
        verbose_name = "Отклик"
        verbose_name_plural = "Отклики"

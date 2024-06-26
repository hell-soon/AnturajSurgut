# Generated by Django 5.0.1 on 2024-04-24 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancy', '0005_responsevacancy_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата обновления'),
        ),
    ]

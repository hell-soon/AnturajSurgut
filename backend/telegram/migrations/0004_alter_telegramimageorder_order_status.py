# Generated by Django 5.0.1 on 2024-02-20 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegram', '0003_telegramimageorder_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telegramimageorder',
            name='order_status',
            field=models.IntegerField(unique=True, verbose_name='Статус заказа'),
        ),
    ]
# Generated by Django 5.0.1 on 2024-02-17 07:44

import database.utils.order_number_generator
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0006_rename_order_adress_order_order_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_address',
            field=models.CharField(blank=True, max_length=255, verbose_name='Адрес доставки'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_number',
            field=models.CharField(default=database.utils.order_number_generator.generate_order_number, max_length=10, unique=True, verbose_name='Номер заказа'),
        ),
    ]

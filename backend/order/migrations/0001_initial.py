# Generated by Django 5.0.1 on 2024-02-28 07:42

import DB.utils.order_number_generator
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('DB', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Additionalservices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название доп.услуги')),
                ('cost', models.FloatField(verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Доп.услуга',
                'verbose_name_plural': 'Доп.услуги',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_initials', models.CharField(max_length=100, verbose_name='Инициалы покупателя')),
                ('user_email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Электронная почта')),
                ('user_phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Номер телефона')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Сформирован')),
                ('order_number', models.CharField(default=DB.utils.order_number_generator.generate_order_number, max_length=10, unique=True, verbose_name='Номер заказа')),
                ('order_type', models.CharField(choices=[('1', 'Самовывоз'), ('2', 'Доставка до двери'), ('3', 'Доставка транспортной компанией')], default='1', max_length=1, verbose_name='Тип доставки')),
                ('order_paymant', models.BooleanField(default=False, verbose_name='Статус оплаты')),
                ('order_address', models.CharField(blank=True, max_length=255, verbose_name='Адрес доставки')),
                ('order_face', models.CharField(choices=[('1', 'Юридическое лицо'), ('2', 'Физическое лицо')], default='1', max_length=1, verbose_name='Тип лица')),
                ('order_status', models.CharField(choices=[('1', 'Не готов'), ('2', 'Готов к выдаче'), ('3', 'Передан в доставку'), ('4', 'Доставлен'), ('5', 'Отменен'), ('6', 'Завершен')], default='1', max_length=1, verbose_name='Статус')),
                ('track_number', models.CharField(blank=True, max_length=255, verbose_name='Номер отслеживания')),
                ('comment', models.TextField(blank=True, verbose_name='Комментарии')),
                ('user_register', models.BooleanField(default=False, verbose_name='Зарегистрирован')),
                ('order_additionalservices', models.ManyToManyField(blank=True, to='order.additionalservices', verbose_name='Доп.услуги')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='OrderItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(blank=True, max_length=100, null=True, verbose_name='Цвет')),
                ('size', models.CharField(blank=True, max_length=100, null=True, verbose_name='Размер')),
                ('cost', models.FloatField(blank=True, null=True, verbose_name='Цена')),
                ('quantity', models.PositiveIntegerField(verbose_name='Количество')),
                ('total_cost', models.FloatField(blank=True, null=True, verbose_name='Общая цена')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.order', verbose_name='номер заказа')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DB.productinfo', verbose_name='Товар')),
            ],
        ),
    ]

# Generated by Django 5.0.1 on 2024-04-04 11:28

import django.db.models.deletion
import order.misc.code_generator
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('DB', '0001_initial'),
        ('sitedb', '0003_alter_contact_options_alter_contact_email'),
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
            name='OrderFace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Тип заказчика',
                'verbose_name_plural': 'Типы заказчиков',
            },
        ),
        migrations.CreateModel(
            name='OrderType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Тип')),
            ],
            options={
                'verbose_name': 'Тип заказа',
                'verbose_name_plural': 'Типы заказов',
            },
        ),
        migrations.CreateModel(
            name='PaymentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Тип оплаты',
                'verbose_name_plural': 'Типы оплаты',
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
                ('order_number', models.CharField(default=order.misc.code_generator.generate_order_number, max_length=10, unique=True, verbose_name='Номер заказа')),
                ('order_paymant', models.BooleanField(default=False, verbose_name='Оплачен')),
                ('order_status', models.CharField(choices=[('1', 'Не готов'), ('2', 'Готов к выдаче'), ('3', 'Передан в доставку'), ('4', 'Доставлен'), ('5', 'Отменен'), ('6', 'Завершен')], default='1', max_length=1, verbose_name='Статус')),
                ('track_number', models.CharField(blank=True, max_length=255, verbose_name='Номер отслеживания')),
                ('comment', models.TextField(blank=True, verbose_name='Комментарии')),
                ('order_additionalservices', models.ManyToManyField(blank=True, to='order.additionalservices', verbose_name='Доп.услуги')),
                ('sertificate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sitedb.sertificate', verbose_name='Сертификат')),
                ('order_face', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.orderface', verbose_name='Тип лица')),
                ('order_type', models.ForeignKey(help_text='При выборе "Самовывоз" адрес заполняется автоматически', on_delete=django.db.models.deletion.CASCADE, to='order.ordertype', verbose_name='Тип доставки')),
                ('payment_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.paymenttype', verbose_name='Способ оплаты')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='OrderAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100, verbose_name='Город')),
                ('region', models.CharField(blank=True, max_length=100, verbose_name='Область')),
                ('street', models.CharField(max_length=100, verbose_name='Улица')),
                ('house', models.CharField(max_length=10, verbose_name='Дом')),
                ('apartment', models.CharField(blank=True, max_length=10, verbose_name='Квартира')),
                ('floor', models.IntegerField(blank=True, null=True, verbose_name='Этаж')),
                ('post_index', models.CharField(blank=True, max_length=6, verbose_name='Почтовый индекс')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.order', verbose_name='номер заказа')),
            ],
            options={
                'verbose_name': 'Адрес',
                'verbose_name_plural': 'Адрес',
            },
        ),
        migrations.CreateModel(
            name='OrderItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(blank=True, max_length=100, null=True, verbose_name='Цвет')),
                ('size', models.CharField(blank=True, max_length=100, null=True, verbose_name='Размер')),
                ('cost', models.FloatField(blank=True, null=True, verbose_name='Цена за шт')),
                ('quantity', models.PositiveIntegerField(verbose_name='Количество')),
                ('total_cost', models.FloatField(blank=True, null=True, verbose_name='Общая цена')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.order', verbose_name='номер заказа')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DB.productinfo', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Детали заказа',
                'verbose_name_plural': 'Детали заказа',
            },
        ),
    ]

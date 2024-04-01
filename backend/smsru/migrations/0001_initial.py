# Generated by Django 5.0.1 on 2024-03-28 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=30, verbose_name='Номер телефона')),
                ('msg', models.TextField(verbose_name='Сообщение')),
                ('status', models.CharField(max_length=10, verbose_name='Статус')),
                ('status_code', models.IntegerField(verbose_name='Код статуса')),
                ('status_text', models.TextField(blank=True, null=True, verbose_name='Текст статуса')),
                ('sms_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='SMS ID')),
                ('cost', models.FloatField(blank=True, null=True, verbose_name='Стоимость')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Лог',
                'verbose_name_plural': 'Логи',
                'ordering': ('-created_at',),
            },
        ),
    ]

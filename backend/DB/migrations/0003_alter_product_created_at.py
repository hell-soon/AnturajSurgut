# Generated by Django 5.0.1 on 2024-04-16 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DB', '0002_alter_product_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Создан'),
        ),
    ]

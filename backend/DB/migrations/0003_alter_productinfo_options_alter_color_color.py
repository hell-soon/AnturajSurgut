# Generated by Django 5.0.1 on 2024-03-10 08:48

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DB', '0002_color_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productinfo',
            options={'verbose_name': 'Информация о продукте', 'verbose_name_plural': 'Линейка товара'},
        ),
        migrations.AlterField(
            model_name='color',
            name='color',
            field=colorfield.fields.ColorField(default='#FFFFFF', image_field=None, max_length=25, samples=None, verbose_name='Код'),
        ),
    ]

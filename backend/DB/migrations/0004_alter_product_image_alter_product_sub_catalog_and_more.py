# Generated by Django 5.0.1 on 2024-03-15 06:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DB', '0003_alter_productinfo_options_alter_color_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ManyToManyField(blank=True, to='DB.productimage', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='product',
            name='sub_catalog',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='DB.subcatalog', verbose_name='Подкаталог'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(upload_to='product_images/', verbose_name='Загрузить картинку'),
        ),
        migrations.AlterField(
            model_name='subcatalog',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='subcatalog_images/', verbose_name='Загрузить картинку'),
        ),
    ]

# Generated by Django 5.0.1 on 2024-02-24 10:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название каталога')),
                ('image', models.ImageField(blank=True, null=True, upload_to='catalog_images/', verbose_name='Картинка')),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Цвет')),
                ('code', models.CharField(max_length=20, verbose_name='Код цвета')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product_images', verbose_name='Картинки товаров')),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Размер')),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название тэга')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Тип')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('product_status', models.BooleanField(default=True, verbose_name='Активен')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('image', models.ManyToManyField(to='DB.productimage', verbose_name='Изображение')),
            ],
        ),
        migrations.CreateModel(
            name='ProductInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('cost', models.FloatField(blank=True, null=True)),
                ('promotion', models.BooleanField(default=False, verbose_name='Товар по акции')),
                ('promotion_cost', models.FloatField(blank=True, null=True, verbose_name='Цена с учетом акции')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DB.color')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DB.product')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DB.size')),
            ],
        ),
        migrations.CreateModel(
            name='SubCatalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название подкаталога')),
                ('image', models.ImageField(blank=True, null=True, upload_to='subcatalog_images')),
                ('catalog', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='DB.catalog', verbose_name='Каталог')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='sub_catalog',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='DB.subcatalog', verbose_name='Подкаталог'),
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(blank=True, to='DB.tags', verbose_name='Тэги'),
        ),
    ]

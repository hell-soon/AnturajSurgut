# Generated by Django 5.0.1 on 2024-02-17 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0004_remove_order_product_order_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='product',
            field=models.ManyToManyField(to='database.product', verbose_name='Товары'),
        ),
    ]

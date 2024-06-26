# Generated by Django 5.0.1 on 2024-05-02 12:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DB', '0012_alter_productinfo_product'),
        ('order', '0010_ordersettings_orderface_settings_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderaddress',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.order', verbose_name='номер заказа'),
        ),
        migrations.AlterField(
            model_name='orderitems',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='DB.productinfo', verbose_name='Товар'),
        ),
    ]

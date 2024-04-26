# Generated by Django 5.0.1 on 2024-04-26 08:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0009_alter_orderitems_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Настройка',
                'verbose_name_plural': 'Настройки',
            },
        ),
        migrations.AddField(
            model_name='orderface',
            name='settings',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='order.ordersettings'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderstatus',
            name='settings',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='order.ordersettings'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ordertype',
            name='settings',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='order.ordersettings'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paymenttype',
            name='settings',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='order.ordersettings'),
            preserve_default=False,
        ),
    ]
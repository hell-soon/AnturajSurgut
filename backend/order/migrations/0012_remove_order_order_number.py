# Generated by Django 5.0.1 on 2024-05-02 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0011_alter_orderaddress_order_alter_orderitems_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_number',
        ),
    ]

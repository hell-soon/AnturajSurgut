# Generated by Django 5.0.1 on 2024-04-24 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_order_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
    ]

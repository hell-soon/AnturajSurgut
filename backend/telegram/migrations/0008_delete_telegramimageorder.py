# Generated by Django 5.0.1 on 2024-03-05 06:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('telegram', '0007_alter_telegramimageorder_order_status'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TelegramImageOrder',
        ),
    ]

# Generated by Django 5.0.1 on 2024-02-25 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_alter_orderitems_color_alter_orderitems_size_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitems',
            name='quantity',
            field=models.PositiveIntegerField(verbose_name='Количество'),
        ),
    ]
# Generated by Django 5.0.1 on 2024-05-02 12:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DB', '0012_alter_productinfo_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinfo',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DB.product', verbose_name='Товар'),
        ),
    ]
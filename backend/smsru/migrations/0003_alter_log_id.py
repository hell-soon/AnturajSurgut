# Generated by Django 5.0.1 on 2024-02-19 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smsru', '0002_fix_log'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

# Generated by Django 5.0.1 on 2024-04-19 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitedb', '0015_contact_latitude_contact_longitude'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='latitude',
            field=models.CharField(max_length=100, verbose_name='Широта'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='longitude',
            field=models.CharField(max_length=100, verbose_name='Долгота'),
        ),
    ]

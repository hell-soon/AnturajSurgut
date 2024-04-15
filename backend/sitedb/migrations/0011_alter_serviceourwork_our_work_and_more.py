# Generated by Django 5.0.1 on 2024-04-09 05:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitedb', '0010_remove_service_our_work_remove_service_slider_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceourwork',
            name='our_work',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='sitedb.ourwork', verbose_name='Наши работы'),
        ),
        migrations.AlterField(
            model_name='serviceslider',
            name='site_image',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='sitedb.siteimage', verbose_name='Картинки для слайдера'),
        ),
    ]

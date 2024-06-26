# Generated by Django 5.0.1 on 2024-04-08 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitedb', '0008_ourworkimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='url',
        ),
        migrations.AddField(
            model_name='service',
            name='our_work',
            field=models.ManyToManyField(blank=True, to='sitedb.ourwork', verbose_name='Наши работы'),
        ),
        migrations.AddField(
            model_name='service',
            name='our_work_is_active',
            field=models.BooleanField(default=True, verbose_name='Активен'),
        ),
    ]

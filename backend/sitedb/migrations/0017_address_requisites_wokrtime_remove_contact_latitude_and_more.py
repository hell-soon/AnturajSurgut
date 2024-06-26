# Generated by Django 5.0.1 on 2024-04-19 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitedb', '0016_alter_contact_latitude_alter_contact_longitude'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес')),
                ('longitude', models.CharField(max_length=100, verbose_name='Долгота')),
                ('latitude', models.CharField(max_length=100, verbose_name='Широта')),
            ],
            options={
                'verbose_name': 'Адрес',
                'verbose_name_plural': 'Адреса',
            },
        ),
        migrations.CreateModel(
            name='Requisites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=255, verbose_name='ИП')),
                ('inn', models.CharField(max_length=255, verbose_name='ИНН')),
                ('legal_address', models.CharField(max_length=255, verbose_name='Юридический адрес')),
            ],
            options={
                'verbose_name': 'Реквизиты',
                'verbose_name_plural': 'Реквизиты',
            },
        ),
        migrations.CreateModel(
            name='WokrTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_time', models.CharField(max_length=255, verbose_name='Время работы')),
            ],
            options={
                'verbose_name': 'Время работы',
                'verbose_name_plural': 'Время работы',
            },
        ),
        migrations.RemoveField(
            model_name='contact',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='longitude',
        ),
    ]

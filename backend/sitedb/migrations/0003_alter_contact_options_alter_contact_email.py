# Generated by Django 5.0.1 on 2024-04-03 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitedb', '0002_contact_socialaccount'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'Контакт', 'verbose_name_plural': 'Контакты'},
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=255, verbose_name='Email'),
        ),
    ]

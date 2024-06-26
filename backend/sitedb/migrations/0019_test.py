# Generated by Django 5.0.1 on 2024-04-22 07:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitedb', '0018_remove_service_table_alter_service_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sitedb.address')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sitedb.contact')),
                ('social_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sitedb.socialaccount')),
                ('work_time', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sitedb.wokrtime')),
            ],
            options={
                'verbose_name': 'Тест',
                'verbose_name_plural': 'Тесты',
            },
        ),
    ]

# Generated by Django 5.0.1 on 2024-04-24 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_user_tg_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='user_tg_id',
            new_name='tg_id',
        ),
    ]
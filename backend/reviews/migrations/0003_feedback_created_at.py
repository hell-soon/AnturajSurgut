# Generated by Django 5.0.1 on 2024-04-19 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0002_feedback"),
    ]

    operations = [
        migrations.AddField(
            model_name="feedback",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=False,
        ),
    ]

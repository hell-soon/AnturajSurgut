# Generated by Django 5.0.1 on 2024-04-20 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DB', '0005_compaundratio_remove_compound_ratio_compound_ratio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compound',
            name='ratio',
        ),
        migrations.AlterField(
            model_name='compound',
            name='name',
            field=models.CharField(max_length=20, verbose_name='Название'),
        ),
        migrations.DeleteModel(
            name='CompaundRatio',
        ),
    ]
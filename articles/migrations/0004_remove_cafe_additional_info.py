# Generated by Django 3.2.13 on 2022-11-03 06:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_remove_cafe_lastorder'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cafe',
            name='additional_info',
        ),
    ]
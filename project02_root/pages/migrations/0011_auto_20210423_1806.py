# Generated by Django 3.1.5 on 2021-04-23 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0010_auto_20210423_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='permalink',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
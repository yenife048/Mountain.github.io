# Generated by Django 3.2.7 on 2023-06-01 01:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0024_remove_hamburguesas_observaciones'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hamburguesas',
            name='precio_ver',
        ),
    ]

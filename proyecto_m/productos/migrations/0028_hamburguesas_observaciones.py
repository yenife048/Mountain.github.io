# Generated by Django 3.2.7 on 2023-06-11 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0027_hamburguesas_descrip'),
    ]

    operations = [
        migrations.AddField(
            model_name='hamburguesas',
            name='observaciones',
            field=models.TextField(default=1, verbose_name='Observacion'),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.2.7 on 2023-07-05 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0031_delete_cajaobservaciones'),
    ]

    operations = [
        migrations.AddField(
            model_name='hamburguesas',
            name='sugerencias',
            field=models.CharField(default=1, max_length=100, verbose_name='sugerencias'),
            preserve_default=False,
        ),
    ]
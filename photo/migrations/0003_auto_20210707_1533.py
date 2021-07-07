# Generated by Django 3.2.5 on 2021-07-07 12:33

import cloudinary.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0002_auto_20210705_0916'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='title',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='images',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]
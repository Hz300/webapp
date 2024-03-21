# Generated by Django 5.0.2 on 2024-03-19 15:03

import web_site.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_site', '0015_alter_asociados_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asociados',
            name='imagen',
            field=models.ImageField(blank=True, upload_to=web_site.models.get_image_path),
        ),
        migrations.AlterField(
            model_name='propertyimage',
            name='image',
            field=models.ImageField(blank=True, db_column='IMAGES', null=True, upload_to=web_site.models.get_image_path),
        ),
    ]

# Generated by Django 2.2.7 on 2019-11-21 18:06

from django.db import migrations, models
import galleries.models.gallery


class Migration(migrations.Migration):

    dependencies = [
        ('galleries', '0003_auto_20191114_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='main_image',
            field=models.FileField(upload_to=galleries.models.gallery.gallery_upload_path),
        ),
    ]

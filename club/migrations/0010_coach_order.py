# Generated by Django 2.2.7 on 2019-11-29 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0009_delete_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='coach',
            name='order',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

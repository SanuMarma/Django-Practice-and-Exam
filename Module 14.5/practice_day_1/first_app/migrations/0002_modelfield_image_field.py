# Generated by Django 5.0.6 on 2024-12-20 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelfield',
            name='image_field',
            field=models.ImageField(null=True, upload_to='first_app/upload'),
        ),
    ]

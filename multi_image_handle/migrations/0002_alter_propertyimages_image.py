# Generated by Django 4.2.5 on 2023-10-30 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multi_image_handle', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertyimages',
            name='image',
            field=models.ImageField(upload_to='PropertyImages/'),
        ),
    ]
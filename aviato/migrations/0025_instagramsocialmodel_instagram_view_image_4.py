# Generated by Django 4.0.4 on 2022-05-01 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aviato', '0024_rename_instagram_view_image_instagramsocialmodel_instagram_view_image_1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='instagramsocialmodel',
            name='instagram_view_image_4',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
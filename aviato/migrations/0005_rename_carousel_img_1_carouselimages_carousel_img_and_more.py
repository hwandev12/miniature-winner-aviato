# Generated by Django 4.0.4 on 2022-04-27 06:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aviato', '0004_rename_image_carouselimages_carousel_img_1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carouselimages',
            old_name='carousel_img_1',
            new_name='carousel_img',
        ),
        migrations.RemoveField(
            model_name='carouselimages',
            name='carousel_img_2',
        ),
        migrations.RemoveField(
            model_name='carouselimages',
            name='carousel_img_3',
        ),
    ]

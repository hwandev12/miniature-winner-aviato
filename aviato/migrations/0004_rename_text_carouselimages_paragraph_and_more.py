# Generated by Django 4.0.4 on 2022-04-29 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aviato', '0003_header_delete_logo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carouselimages',
            old_name='text',
            new_name='paragraph',
        ),
        migrations.AddField(
            model_name='carouselimages',
            name='menu',
            field=models.TextField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]

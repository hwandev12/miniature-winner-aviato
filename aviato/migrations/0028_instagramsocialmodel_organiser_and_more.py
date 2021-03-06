# Generated by Django 4.0.4 on 2022-05-01 08:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aviato', '0027_rename_instagram_view_image_1_instagramsocialmodel_instagram_view_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='instagramsocialmodel',
            name='organiser',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='aviato.userprofile'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='InstagramCategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instagram_category_name', models.CharField(max_length=200)),
                ('organiser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aviato.userprofile')),
            ],
            options={
                'verbose_name': 'Instagram Category',
            },
        ),
        migrations.AddField(
            model_name='instagramsocialmodel',
            name='instagram_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='aviato.instagramcategorymodel'),
        ),
    ]

# Generated by Django 4.0.4 on 2022-04-30 01:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aviato', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategory',
            name='category_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='aviato.productsinglecategory'),
        ),
    ]

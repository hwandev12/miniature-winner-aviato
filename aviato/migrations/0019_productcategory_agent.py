# Generated by Django 4.0.4 on 2022-04-30 06:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aviato', '0018_alter_productcategory_category_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcategory',
            name='agent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='aviato.agent'),
        ),
    ]

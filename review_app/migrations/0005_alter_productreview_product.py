# Generated by Django 4.0.1 on 2022-03-02 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review_app', '0004_wichlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productreview',
            name='product',
            field=models.IntegerField(),
        ),
    ]

# Generated by Django 4.0.1 on 2022-02-28 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PopUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=150)),
            ],
        ),
    ]
# Generated by Django 3.0.5 on 2020-04-12 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200411_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantprofile',
            name='address',
            field=models.TextField(blank=True),
        ),
    ]
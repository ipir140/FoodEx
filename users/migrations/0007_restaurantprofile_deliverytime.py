# Generated by Django 3.0.5 on 2020-04-13 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20200412_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantprofile',
            name='deliveryTime',
            field=models.IntegerField(default=20),
        ),
    ]

# Generated by Django 3.0.5 on 2020-04-13 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20200413_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerreviews',
            name='ratings',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=1),
        ),
    ]

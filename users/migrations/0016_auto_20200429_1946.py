# Generated by Django 3.0.5 on 2020-04-29 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_restaurantprofile_minimumorder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerprofile',
            name='image',
            field=models.ImageField(default='default_user_pic.jpg', upload_to='profile_pics/'),
        ),
    ]
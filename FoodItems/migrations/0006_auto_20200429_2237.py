# Generated by Django 3.0.5 on 2020-04-29 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FoodItems', '0005_foodcategory_categorydescription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordersdescription',
            name='Subtotal',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='ordersdescription',
            name='TotalPrice',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='ordersdescription',
            name='charges',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='ordersdescription',
            name='received',
            field=models.FloatField(),
        ),
    ]

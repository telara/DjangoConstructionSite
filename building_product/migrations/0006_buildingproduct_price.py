# Generated by Django 2.2.8 on 2019-12-14 12:03

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('building_product', '0005_auto_20191214_1140'),
    ]

    operations = [
        migrations.AddField(
            model_name='buildingproduct',
            name='price',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.0000'), max_digits=10),
        ),
    ]
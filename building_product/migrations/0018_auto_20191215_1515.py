# Generated by Django 2.2.8 on 2019-12-15 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('building_product', '0017_auto_20191214_1347'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buildingproduct',
            old_name='photo_thumbnail',
            new_name='photo',
        ),
    ]

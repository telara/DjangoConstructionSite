# Generated by Django 2.2.8 on 2019-12-14 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('building_product', '0002_auto_20191214_1116'),
    ]

    operations = [
        migrations.AddField(
            model_name='buildingproduct',
            name='company_logo',
            field=models.ImageField(default='settings/media/product_photos/TaraElsen_wZKfXJQ.jpg', upload_to='company_logos'),
        ),
    ]

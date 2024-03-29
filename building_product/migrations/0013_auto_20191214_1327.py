# Generated by Django 2.2.8 on 2019-12-14 13:27

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('building_product', '0012_auto_20191214_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buildingproduct',
            name='company_logo_thumbnail',
            field=imagekit.models.fields.ProcessedImageField(default='product_photos/default.jpg', upload_to='company_logos'),
        ),
        migrations.AlterField(
            model_name='buildingproduct',
            name='photo_thumbnail',
            field=imagekit.models.fields.ProcessedImageField(default='product_photos/default_photo.jpg', upload_to='product_photos'),
        ),
    ]

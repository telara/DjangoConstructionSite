# Generated by Django 2.2.8 on 2019-12-14 13:30

from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('building_product', '0013_auto_20191214_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buildingproduct',
            name='company_logo_thumbnail',
            field=imagekit.models.fields.ProcessedImageField(default='company_logos/default.jpg', upload_to='company_logos'),
        ),
        migrations.AlterField(
            model_name='buildingproduct',
            name='school_type',
            field=models.CharField(choices=[('MBO', 'MBO'), ('VMBO', 'VMBO'), ('HBO', 'HBO'), ('Opleidingsbedrijf', 'Opleidingsbedrijf')], max_length=20),
        ),
    ]

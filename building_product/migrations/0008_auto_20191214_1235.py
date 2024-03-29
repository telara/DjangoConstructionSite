# Generated by Django 2.2.8 on 2019-12-14 12:35

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('building_product', '0007_buildingproduct_company_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buildingproduct',
            name='categories',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('MATERIALS', 'Materials'), ('COURSE', 'Course')], default='COURSE', max_length=16),
        ),
        migrations.AlterField(
            model_name='buildingproduct',
            name='company_logo',
            field=models.ImageField(upload_to='company_logos'),
        ),
        migrations.AlterField(
            model_name='buildingproduct',
            name='company_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='buildingproduct',
            name='expiration_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='buildingproduct',
            name='school_type',
            field=models.CharField(choices=[('MBO', 'MBO'), ('VMBO', 'VMBO'), ('HBO', 'HBO'), ('OPLEIDINGSBEDRIJF', 'Opleidingsbedrijf')], max_length=20),
        ),
    ]

# Generated by Django 2.2.8 on 2019-12-13 13:04

from django.db import migrations, models
import django.utils.timezone
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BuildingProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('photo', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('company_logo', models.CharField(max_length=200)),
                ('categories', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('MATERIALS', 'Materials'), ('COURSE', 'Course')], max_length=16)),
                ('schooltype', models.CharField(choices=[('MBO', 'MBO'), ('VMBO', 'VMBO'), ('HBO', 'HBO'), ('OPLEIDINGSBEDRIJF', 'Opleidingsbedrijf')], default='MBO', max_length=20)),
                ('expiration_date', models.DateTimeField(blank=True, null=True)),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]

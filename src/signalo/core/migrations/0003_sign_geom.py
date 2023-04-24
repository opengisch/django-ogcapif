# Generated by Django 4.2 on 2023-04-21 15:36

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signalo_core', '0002_remove_sign_geom_azimuth_geom'),
    ]

    operations = [
        migrations.AddField(
            model_name='sign',
            name='geom',
            field=django.contrib.gis.db.models.fields.PointField(editable=False, null=True, srid=2056, verbose_name='Geometry'),
        ),
    ]
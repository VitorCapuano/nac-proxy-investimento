# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-01 05:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_adquirente_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adquirente',
            name='total',
            field=models.DecimalField(decimal_places=2, editable=False, max_digits=12),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-25 17:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0002_auto_20170225_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry_rate',
            name='entry_type_r',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='club.Entry_Type'),
        ),
    ]

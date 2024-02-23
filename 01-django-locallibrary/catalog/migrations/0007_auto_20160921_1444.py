# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-21 04:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0006_auto_20160921_1439"),
    ]

    operations = [
        migrations.AlterField(
            model_name="author",
            name="date_of_birth",
            field=models.DateField(blank=True, null=True, verbose_name="D.O.B"),
        ),
        migrations.AlterField(
            model_name="author",
            name="date_of_death",
            field=models.DateField(blank=True, null=True, verbose_name="Died"),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-05 10:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0016_auto_20160927_1947"),
    ]

    operations = [
        migrations.CreateModel(
            name="Language",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Enter a the book's natural language (e.g. English, French, Japanese etc.)",
                        max_length=200,
                    ),
                ),
            ],
        ),
    ]

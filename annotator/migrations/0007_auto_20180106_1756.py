# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-06 17:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annotator', '0006_auto_20180106_1743'),
    ]

    operations = [
        migrations.AddField(
            model_name='wordoption',
            name='isEliminated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='wordoption',
            name='isSelected',
            field=models.BooleanField(default=False),
        ),
    ]

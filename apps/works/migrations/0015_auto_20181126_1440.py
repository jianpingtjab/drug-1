# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-26 14:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0014_auto_20181126_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autoduck',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

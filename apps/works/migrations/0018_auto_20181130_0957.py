# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-30 09:57
from __future__ import unicode_literals

from django.db import migrations, models
import works.models


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0017_auto_20181130_0909'),
    ]

    operations = [
        migrations.AddField(
            model_name='autoduck2',
            name='status',
            field=models.CharField(default='\u6392\u961f\u4e2d', max_length=10, verbose_name='status'),
        ),
        migrations.AddField(
            model_name='virtualscreen',
            name='status',
            field=models.CharField(default='\u6392\u961f\u4e2d', max_length=10, verbose_name='status'),
        ),
        migrations.AddField(
            model_name='virtualscreen2',
            name='status',
            field=models.CharField(default='\u6392\u961f\u4e2d', max_length=10, verbose_name='status'),
        ),
        migrations.AlterField(
            model_name='virtualscreen',
            name='user_db',
            field=models.FileField(default=0, upload_to=works.models.upload_to, verbose_name='user_db'),
        ),
        migrations.AlterField(
            model_name='virtualscreen',
            name='work_decs',
            field=models.CharField(max_length=100, verbose_name='work_decs'),
        ),
        migrations.AlterField(
            model_name='virtualscreen2',
            name='mol_db',
            field=models.CharField(choices=[(1, 'zinc'), (2, 'chembl'), (3, 'wi')], default=0, max_length=10, null=True, verbose_name='mol_db'),
        ),
        migrations.AlterField(
            model_name='virtualscreen2',
            name='user_db',
            field=models.FileField(default=0, upload_to=works.models.upload_to, verbose_name='user_db'),
        ),
    ]

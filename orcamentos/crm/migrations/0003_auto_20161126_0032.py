# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-11-26 02:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_auto_20161126_0030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='company',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='empresa'),
        ),
        migrations.AlterField(
            model_name='person',
            name='company',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='empresa'),
        ),
    ]
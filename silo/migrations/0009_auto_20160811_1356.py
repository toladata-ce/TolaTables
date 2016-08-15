# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-08-11 20:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('silo', '0008_auto_20160811_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='read',
            name='password',
            field=models.CharField(blank=True, help_text=b'Enter password only if the data at this source is protected by a login', max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='read',
            name='username',
            field=models.CharField(blank=True, help_text=b'Enter username only if the data at this source is protected by a login', max_length=20, null=True),
        ),
    ]

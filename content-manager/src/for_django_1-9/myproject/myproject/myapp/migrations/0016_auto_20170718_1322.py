# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-18 03:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_auto_20170718_1318'),
    ]

    operations = [
        migrations.RenameField(
            model_name='week',
            old_name='test',
            new_name='week',
        ),
    ]

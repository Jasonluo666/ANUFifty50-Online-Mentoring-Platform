# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-04 00:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pair', '0009_auto_20170703_2349'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Mentee',
        ),
        migrations.DeleteModel(
            name='Mentor',
        ),
    ]

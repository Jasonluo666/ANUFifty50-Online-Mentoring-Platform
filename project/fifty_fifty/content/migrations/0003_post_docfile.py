# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-03 05:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_mentee_mentor'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='docfile',
            field=models.FileField(null=True, upload_to='news/'),
        ),
    ]

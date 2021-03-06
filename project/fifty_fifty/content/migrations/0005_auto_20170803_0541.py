# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-03 05:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_auto_20170803_0535'),
    ]

    operations = [
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('docfile', models.FileField(null=True, upload_to='training/')),
            ],
        ),
        migrations.RemoveField(
            model_name='mentee',
            name='text',
        ),
        migrations.RemoveField(
            model_name='mentor',
            name='text',
        ),
        migrations.AddField(
            model_name='mentee',
            name='docfile',
            field=models.FileField(null=True, upload_to='mentee/'),
        ),
        migrations.AddField(
            model_name='mentor',
            name='docfile',
            field=models.FileField(null=True, upload_to='mentor/'),
        ),
    ]

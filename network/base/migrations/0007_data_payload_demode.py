# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-06 12:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_auto_20160325_0126'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='payload_demode',
            field=models.FileField(blank=True, null=True, upload_to=b'data_payloads'),
        ),
    ]

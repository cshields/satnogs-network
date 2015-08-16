# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.core.management import call_command


def rename_transponders(apps, schema_editor):
    call_command('fetch_data')
    

class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20150723_1416'),
    ]

    operations = [
        migrations.RunPython(rename_transponders),
    ]

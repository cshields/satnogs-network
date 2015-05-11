# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_auto_20150209_0846'),
    ]

    operations = [
        migrations.AddField(
            model_name='station',
            name='qthlocator',
            field=models.CharField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
    ]

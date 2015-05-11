# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import now


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_satellite_tle'),
    ]

    operations = [
        migrations.AddField(
            model_name='satellite',
            name='updated',
            field=models.DateTimeField(default=now(), auto_now_add=True),
            preserve_default=False,
        ),
    ]

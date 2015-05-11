# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import shortuuidfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0016_auto_20150506_1002'),
    ]

    operations = [
        migrations.AddField(
            model_name='transponder',
            name='uuid',
            field=shortuuidfield.fields.ShortUUIDField(db_index=True, max_length=22, editable=False, blank=True),
        ),
        migrations.AlterField(
            model_name='transponder',
            name='mode',
            field=models.CharField(blank=True, max_length=10, choices=[(b'FM', b'FM'), (b'AFSK', b'AFSK'), (b'BFSK', b'BFSK'), (b'APRS', b'APRS'), (b'SSTV', b'SSTV'), (b'CW', b'CW'), (b'FMN', b'FMN'), (b'SSTV', b'SSTV'), (b'GMSK', b'GMSK'), (b'SSB', b'SSB')]),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import shortuuidfield.fields
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20150622_0035'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transmitter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uuid', shortuuidfield.fields.ShortUUIDField(db_index=True, max_length=22, editable=False, blank=True)),
                ('description', models.TextField()),
                ('alive', models.BooleanField(default=True)),
                ('uplink_low', models.PositiveIntegerField(null=True, blank=True)),
                ('uplink_high', models.PositiveIntegerField(null=True, blank=True)),
                ('downlink_low', models.PositiveIntegerField(null=True, blank=True)),
                ('downlink_high', models.PositiveIntegerField(null=True, blank=True)),
                ('mode', models.CharField(blank=True, max_length=10, choices=[(b'FM', b'FM'), (b'AFSK', b'AFSK'), (b'BFSK', b'BFSK'), (b'APRS', b'APRS'), (b'SSTV', b'SSTV'), (b'CW', b'CW'), (b'FMN', b'FMN'), (b'SSTV', b'SSTV'), (b'GMSK', b'GMSK'), (b'SSB', b'SSB')])),
                ('invert', models.BooleanField(default=False)),
                ('baud', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('satellite', models.ForeignKey(related_name='transmitters', to='base.Satellite', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='observation',
            name='transmitter',
            field=models.ForeignKey(to='base.Transmitter', null=True),
        ),
    ]

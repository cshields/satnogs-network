# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_station_qthlocator'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='data',
            options={'ordering': ['-start', '-end']},
        ),
        migrations.AlterModelOptions(
            name='observation',
            options={'ordering': ['-start', '-end']},
        ),
        migrations.AlterModelOptions(
            name='satellite',
            options={'ordering': ['norad_cat_id']},
        ),
        migrations.AlterModelOptions(
            name='station',
            options={'ordering': ['-active', '-last_seen']},
        ),
        migrations.RemoveField(
            model_name='station',
            name='online',
        ),
        migrations.AddField(
            model_name='station',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='station',
            name='last_seen',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='satellite',
            name='tle0',
            field=models.CharField(default='', max_length=100, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='satellite',
            name='tle1',
            field=models.CharField(default='', max_length=200, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='satellite',
            name='tle2',
            field=models.CharField(default='', max_length=200, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='satellite',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='station',
            name='antenna',
            field=models.ManyToManyField(help_text=b'If you want to add a new Antenna contact SatNOGS Team', to='base.Antenna', blank=True),
        ),
        migrations.AlterField(
            model_name='station',
            name='location',
            field=models.CharField(default='', max_length=255, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='station',
            name='qthlocator',
            field=models.CharField(default='', max_length=255, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='transponder',
            name='baud',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='transponder',
            name='mode',
            field=models.CharField(blank=True, max_length=10, choices=[(b'FM', b'FM'), (b'AFSK', b'AFSK'), (b'BFSK', b'BFSK'), (b'APRS', b'APRS'), (b'SSTV', b'SSTV'), (b'CW', b'CW'), (b'FMN', b'FMN')]),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
import shortuuidfield.fields
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    replaces = [(b'base', '0001_initial'), (b'base', '0002_auto_20141015_0800'), (b'base', '0003_auto_20141016_0506'), (b'base', '0004_satellite_tle'), (b'base', '0005_satellite_updated'), (b'base', '0006_auto_20141025_2010'), (b'base', '0007_auto_20141027_0000'), (b'base', '0008_auto_20141027_0113'), (b'base', '0009_auto_20141027_1522'), (b'base', '0010_station_location'), (b'base', '0011_station_created'), (b'base', '0012_auto_20141203_1805'), (b'base', '0013_remove_station_featured'), (b'base', '0014_auto_20150209_0846'), (b'base', '0015_station_qthlocator'), (b'base', '0016_auto_20150506_1002'), (b'base', '0017_auto_20150509_0912')]

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Antenna',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('frequency', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('band', models.CharField(max_length=5, choices=[(b'HF', b'HF'), (b'VHF', b'VHF'), (b'UHF', b'UHF'), (b'L', b'L'), (b'S', b'S'), (b'C', b'C'), (b'X', b'X'), (b'KU', b'KU')])),
                ('antenna_type', models.CharField(max_length=15, choices=[(b'dipole', b'Dipole'), (b'yagi', b'Yagi'), (b'helical', b'Helical'), (b'parabolic', b'Parabolic')])),
            ],
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('payload', models.FileField(upload_to=b'data_payloads')),
            ],
        ),
        migrations.CreateModel(
            name='Observation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Satellite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('norad_cat_id', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=45)),
                ('image', models.ImageField(upload_to=b'ground_stations', blank=True)),
                ('alt', models.PositiveIntegerField(help_text=b'In meters above ground')),
                ('lat', models.FloatField(validators=[django.core.validators.MaxValueValidator(90), django.core.validators.MinValueValidator(-90)])),
                ('lng', models.FloatField(validators=[django.core.validators.MaxValueValidator(180), django.core.validators.MinValueValidator(-180)])),
                ('featured_date', models.DateField(null=True, blank=True)),
                ('antenna', models.ManyToManyField(help_text=b'If you want to add a new Antenna contact SatNOGS Team', to=b'base.Antenna', null=True, blank=True)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('location', models.CharField(max_length=255, null=True, blank=True)),
                ('created', models.DateTimeField(default=datetime.datetime(2015, 6, 9, 15, 56, 50, 800909, tzinfo=utc), auto_now_add=True)),
                ('online', models.BooleanField(default=False, help_text=b'Is your Ground Station functional?')),
                ('qthlocator', models.CharField(max_length=255, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transponder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField()),
                ('alive', models.BooleanField(default=True)),
                ('uplink_low', models.PositiveIntegerField(null=True, blank=True)),
                ('uplink_high', models.PositiveIntegerField(null=True, blank=True)),
                ('downlink_low', models.PositiveIntegerField(null=True, blank=True)),
                ('downlink_high', models.PositiveIntegerField(null=True, blank=True)),
                ('mode', models.CharField(blank=True, max_length=10, choices=[(b'FM', b'FM'), (b'AFSK', b'AFSK'), (b'BFSK', b'BFSK'), (b'APRS', b'APRS'), (b'SSTV', b'SSTV'), (b'CW', b'CW'), (b'FMN', b'FMN'), (b'SSTV', b'SSTV'), (b'GMSK', b'GMSK'), (b'SSB', b'SSB')])),
                ('invert', models.BooleanField(default=False)),
                ('baud', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('satellite', models.ForeignKey(related_name=b'transponder', to='base.Satellite', null=True)),
                ('uuid', shortuuidfield.fields.ShortUUIDField(db_index=True, max_length=22, editable=False, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='observation',
            name='satellite',
            field=models.ForeignKey(to='base.Satellite'),
        ),
        migrations.AddField(
            model_name='observation',
            name='transponder',
            field=models.ForeignKey(to='base.Transponder', null=True),
        ),
        migrations.AddField(
            model_name='data',
            name='ground_station',
            field=models.ForeignKey(to='base.Station'),
        ),
        migrations.AddField(
            model_name='data',
            name='observation',
            field=models.ForeignKey(to='base.Observation'),
        ),
        migrations.AddField(
            model_name='satellite',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 9, 15, 56, 50, 787197, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='satellite',
            name='tle0',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='satellite',
            name='tle1',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='satellite',
            name='tle2',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='payload',
            field=models.FileField(null=True, upload_to=b'data_payloads'),
        ),
        migrations.AlterField(
            model_name='data',
            name='payload',
            field=models.FileField(null=True, upload_to=b'data_payloads', blank=True),
        ),
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
            field=models.ManyToManyField(help_text=b'If you want to add a new Antenna contact SatNOGS Team', to=b'base.Antenna', blank=True),
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
    ]

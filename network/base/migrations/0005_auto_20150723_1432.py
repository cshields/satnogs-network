# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def mv_observations(apps, schema_editor):
    Observation = apps.get_model("base", "Observation")
    Transmitter = apps.get_model("base", "Transmitter")
    for obj in Observation.objects.all():
        try:
            transmitter = Transmitter.objects.get(uuid=obj.transponder.uuid)
            obj.transmitter = transmitter
            obj.save()
        except Transmitter.DoesNotExist:
            pass


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_auto_20150723_1412'),
    ]

    operations = [
        migrations.RunPython(mv_observations),
    ]

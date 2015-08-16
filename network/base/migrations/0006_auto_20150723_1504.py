# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_auto_20150723_1432'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transponder',
            name='satellite',
        ),
        migrations.RemoveField(
            model_name='observation',
            name='transponder',
        ),
        migrations.AlterField(
            model_name='observation',
            name='transmitter',
            field=models.ForeignKey(related_name='observations', to='base.Transmitter', null=True),
        ),
        migrations.DeleteModel(
            name='Transponder',
        ),
    ]

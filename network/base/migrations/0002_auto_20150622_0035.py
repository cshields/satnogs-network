# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_squashed_0017_auto_20150509_0912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='station',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

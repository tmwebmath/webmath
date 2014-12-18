# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0002_auto_20141208_1417'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exercise',
            old_name='author',
            new_name='owner',
        ),
        migrations.RenameField(
            model_name='skill',
            old_name='skill',
            new_name='description',
        ),
        migrations.AddField(
            model_name='skill',
            name='short_name',
            field=models.CharField(max_length=30, default=datetime.date(2014, 12, 18)),
            preserve_default=False,
        ),
    ]

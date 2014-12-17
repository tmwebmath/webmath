# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20141211_0858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='html_content',
            field=models.TextField(blank=True),
        ),
    ]

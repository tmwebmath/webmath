# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20141208_1417'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='section',
            name='content',
        ),
        migrations.AddField(
            model_name='section',
            name='html_content',
            field=models.TextField(default=''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='section',
            name='markdown_content',
            field=models.TextField(default=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='favorites',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL, related_name='favorite_courses'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0001_initial'),
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='author',
            field=models.ForeignKey(related_name='courses', to='teachers.Teacher'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='course',
            name='chapter',
            field=models.ForeignKey(related_name='courses', to='teachers.Chapter'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='course',
            name='favorites',
            field=models.ManyToManyField(related_name='favorite_courses', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]

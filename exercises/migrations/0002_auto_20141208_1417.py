# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0001_initial'),
        ('students', '0001_initial'),
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='chapter',
            field=models.ManyToManyField(to='teachers.Chapter'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='exercise_type',
            name='skill',
            field=models.ManyToManyField(to='exercises.Skill'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='exercise_type',
            name='user',
            field=models.ManyToManyField(to='students.Student'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='exercise',
            name='author',
            field=models.ForeignKey(to='teachers.Teacher'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='exercise',
            name='chapter',
            field=models.ManyToManyField(to='teachers.Chapter'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='exercise',
            name='type_donnees',
            field=models.ForeignKey(to='exercises.Exercise_type'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='exercise',
            name='user',
            field=models.ManyToManyField(to='students.Student'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='correction',
            name='exercise',
            field=models.ForeignKey(to='exercises.Exercise'),
            preserve_default=True,
        ),
    ]

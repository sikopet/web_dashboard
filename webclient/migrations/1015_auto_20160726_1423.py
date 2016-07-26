# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-26 14:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webclient', '1014_auto_20160726_1422'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imagewindow',
            old_name='length',
            new_name='width',
        ),
        migrations.AlterUniqueTogether(
            name='imagewindow',
            unique_together=set([('x', 'y', 'width', 'height')]),
        ),
    ]

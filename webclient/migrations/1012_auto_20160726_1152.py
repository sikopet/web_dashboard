# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-26 11:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webclient', '1011_auto_20160719_1502'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='length',
            field=models.PositiveSmallIntegerField(default=1920),
        ),
        migrations.AddField(
            model_name='image',
            name='width',
            field=models.PositiveSmallIntegerField(default=1080),
        ),
    ]

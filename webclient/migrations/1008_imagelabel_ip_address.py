# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-15 15:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webclient', '1007_auto_20160707_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagelabel',
            name='ip_address',
            field=models.GenericIPAddressField(blank=True, default=None, null=True),
        ),
    ]

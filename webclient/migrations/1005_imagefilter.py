# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-29 18:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webclient', '1004_auto_20160531_1529'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageFilter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brightness', models.DecimalField(decimal_places=1, max_digits=3)),
                ('contrast', models.DecimalField(decimal_places=1, max_digits=3)),
                ('saturation', models.DecimalField(decimal_places=1, max_digits=3)),
            ],
        ),
    ]

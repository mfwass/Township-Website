# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-25 21:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('township', '0003_auto_20170525_1804'),
    ]

    operations = [
        migrations.AddField(
            model_name='newspost',
            name='viewable',
            field=models.BooleanField(default=True),
        ),
    ]
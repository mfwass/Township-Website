# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-25 17:46
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('township', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitebanner',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='newspost',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]

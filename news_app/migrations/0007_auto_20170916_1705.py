# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-16 17:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0006_auto_20170916_1645'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='published_at',
            new_name='published_date',
        ),
    ]

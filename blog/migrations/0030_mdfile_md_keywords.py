# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-12 23:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0029_auto_20160801_1222'),
    ]

    operations = [
        migrations.AddField(
            model_name='mdfile',
            name='md_keywords',
            field=models.CharField(blank=True, max_length=128, verbose_name=b'Keywords'),
        ),
    ]

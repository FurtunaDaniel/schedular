# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-23 14:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20170423_1112'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='CNP',
            field=models.CharField(blank=True, max_length=25, verbose_name='CNP'),
        ),
    ]

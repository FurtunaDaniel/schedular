# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-21 22:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='last name')),
                ('email', models.EmailField(blank=True, db_index=True, max_length=255, null=True, unique=True, verbose_name='email address')),
                ('username', models.CharField(blank=True, db_index=True, max_length=255, null=True, unique=True, verbose_name='username')),
                ('address', models.CharField(blank=True, max_length=300, null=True, verbose_name='address')),
                ('phone_number', models.CharField(blank=True, max_length=25, verbose_name='phone number')),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('alert_email', models.BooleanField(default=False)),
                ('alert_sms', models.BooleanField(default=False)),
                ('is_student', models.BooleanField(default=False)),
                ('is_teacher', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

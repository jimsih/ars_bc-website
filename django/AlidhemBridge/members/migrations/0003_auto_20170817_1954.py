# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-17 19:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_auto_20170817_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='portrait',
            field=models.FileField(blank=True, null=True, upload_to='member_portraits/'),
        ),
    ]
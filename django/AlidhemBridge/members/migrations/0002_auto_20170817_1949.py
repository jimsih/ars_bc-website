# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-17 19:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='email',
            field=models.EmailField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='member',
            name='last_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='member',
            name='office',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='member',
            name='portrait',
            field=models.FileField(null=True, upload_to='member_portraits/'),
        ),
    ]

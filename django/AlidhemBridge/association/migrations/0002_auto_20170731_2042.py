# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-31 18:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('association', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statute',
            name='date',
            field=models.DateField(verbose_name='date'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-24 05:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='first_name_kan',
            field=models.CharField(default=0, max_length=20, verbose_name='名'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name_kan',
            field=models.CharField(max_length=20, verbose_name='姓'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-10 05:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0020_auto_20161023_0851'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdevelopenvironmentskill',
            name='delflg',
            field=models.BooleanField(default=1, verbose_name='削除フラグ'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprogrammingskill',
            name='delflg',
            field=models.BooleanField(default=False, verbose_name='削除フラグ'),
        ),
    ]
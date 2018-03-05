# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-02 00:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0008_auto_20161002_0145'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=50, verbose_name='性別')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.IntegerField(default=0, verbose_name='年齢'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='subprojectoverview',
            name='comment',
            field=models.CharField(max_length=200, verbose_name='プロジェクト概要'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='name',
            field=models.CharField(max_length=128, verbose_name='会社名'),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cms.Gender'),
        ),
    ]
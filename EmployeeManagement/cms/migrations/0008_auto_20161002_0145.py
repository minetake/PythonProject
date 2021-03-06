# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-01 16:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0007_auto_20161002_0050'),
    ]

    operations = [
        migrations.CreateModel(
            name='DevelopEnvironment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='名前')),
            ],
        ),
        migrations.CreateModel(
            name='ProgrammingLanguage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='名前')),
            ],
        ),
        migrations.CreateModel(
            name='SubProjectEnvironmentSkill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='SubProjectProgrammingSkill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='UserDevelopEnvironmentSkill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(max_length=50, verbose_name='バージョン')),
                ('years', models.IntegerField(verbose_name='経験年数')),
                ('environment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cms.DevelopEnvironment')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cms.User')),
            ],
        ),
        migrations.CreateModel(
            name='UserProgrammingSkill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(max_length=50, verbose_name='バーション')),
                ('years', models.IntegerField(verbose_name='経験年数')),
                ('program', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cms.ProgrammingLanguage')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cms.User')),
            ],
        ),
        migrations.RemoveField(
            model_name='project',
            name='scale',
        ),
        migrations.AddField(
            model_name='subprojectoverview',
            name='scale',
            field=models.IntegerField(blank=True, null=True, verbose_name='規模'),
        ),
        migrations.AddField(
            model_name='subprojectprogrammingskill',
            name='program',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cms.UserProgrammingSkill'),
        ),
        migrations.AddField(
            model_name='subprojectprogrammingskill',
            name='subproject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cms.SubProjectOverview'),
        ),
        migrations.AddField(
            model_name='subprojectenvironmentskill',
            name='environment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cms.UserDevelopEnvironmentSkill'),
        ),
        migrations.AddField(
            model_name='subprojectenvironmentskill',
            name='subproject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cms.SubProjectOverview'),
        ),
    ]

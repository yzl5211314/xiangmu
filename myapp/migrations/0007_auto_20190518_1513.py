# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-18 07:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_remove_kecheng_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='dagang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='教学大纲标题')),
            ],
            options={
                'verbose_name_plural': '教学大纲标题',
                'verbose_name': '教学大纲标题',
            },
        ),
        migrations.AddField(
            model_name='xiangqing',
            name='title',
            field=models.CharField(default=1, max_length=64, verbose_name='课程介绍详情标题'),
            preserve_default=False,
        ),
    ]

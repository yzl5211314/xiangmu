# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-17 16:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20190517_2257'),
    ]

    operations = [
        migrations.CreateModel(
            name='teachers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover', models.ImageField(upload_to='static/imgs/teachers', verbose_name='教师列表图片')),
                ('name', models.CharField(max_length=64, verbose_name='教师名字')),
            ],
            options={
                'verbose_name_plural': '教师列表',
                'verbose_name': '教师列表',
            },
        ),
    ]

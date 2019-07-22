# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-18 08:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20190518_1513'),
    ]

    operations = [
        migrations.CreateModel(
            name='kejian',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='教学课件标题')),
                ('cover', models.ImageField(upload_to='static/imgs/kejian', verbose_name='教学课件图片')),
                ('content', models.TextField(verbose_name='教学课件内容')),
            ],
            options={
                'verbose_name': '教学课件',
                'verbose_name_plural': '教学课件',
            },
        ),
        migrations.AlterModelOptions(
            name='dagang',
            options={'verbose_name': '教学大纲', 'verbose_name_plural': '教学大纲'},
        ),
    ]

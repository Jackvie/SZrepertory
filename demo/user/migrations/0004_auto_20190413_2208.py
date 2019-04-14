# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-04-13 14:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_bookinfo_heroinfo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='areas',
            options={'verbose_name': '地区表', 'verbose_name_plural': '地区表'},
        ),
        migrations.AlterModelOptions(
            name='picupload',
            options={'verbose_name': '上传图片', 'verbose_name_plural': '上传图片'},
        ),
        migrations.AddField(
            model_name='bookinfo',
            name='image',
            field=models.ImageField(null=True, upload_to='booktest', verbose_name='图片'),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-11 09:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='author',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='articles',
            name='create_time',
            field=models.CharField(default='', max_length=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='articles',
            name='desc',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]

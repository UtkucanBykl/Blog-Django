# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-15 18:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_post_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='body',
            field=models.CharField(default='d', max_length=140),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='d', upload_to=''),
            preserve_default=False,
        ),
    ]
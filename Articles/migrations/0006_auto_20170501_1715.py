# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-01 17:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Articles', '0005_auto_20170416_1755'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-date']},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-date']},
        ),
        migrations.AddField(
            model_name='comment',
            name='like',
            field=models.IntegerField(default=0),
        ),
    ]

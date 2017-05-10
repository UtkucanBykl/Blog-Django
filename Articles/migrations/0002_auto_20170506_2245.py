# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-06 22:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Articles', '0001_initial'),
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
            model_name='article',
            name='like',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='comment',
            name='comcom',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='com', to='Articles.Comment'),
        ),
        migrations.AlterUniqueTogether(
            name='article',
            unique_together=set([('title', 'body')]),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-18 14:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25, unique=True)),
                ('body', models.CharField(max_length=140, unique=True)),
                ('content', models.TextField()),
                ('like', models.IntegerField(default=0)),
                ('genre', models.CharField(max_length=10)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('publish', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('comment', models.TextField(max_length=140)),
                ('publish', models.BooleanField(default=False)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='Articles.Article')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]

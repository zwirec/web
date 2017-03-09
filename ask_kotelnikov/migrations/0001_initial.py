# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-07 14:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('is_correct', models.NullBooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('text', models.TextField()),
                ('rate', models.IntegerField()),
                ('pub_date', models.DateTimeField()),
                ('answers', models.ManyToManyField(to='ask_kotelnikov.Answer')),
            ],
        ),
    ]

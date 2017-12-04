# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-03 18:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='question',
            new_name='together',
        ),
        migrations.RemoveField(
            model_name='question',
            name='guestion_text',
        ),
        migrations.AddField(
            model_name='question',
            name='question_text',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 3, 19, 25, 33, 120351)),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-22 22:43
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pufin', '0005_auto_20170322_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='Published',
            field=models.DateField(default=datetime.date.today),
        ),
    ]

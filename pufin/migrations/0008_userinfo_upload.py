# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-22 23:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pufin', '0007_auto_20170322_2257'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='upload',
            field=models.FileField(default=0, upload_to=b'uploads/'),
            preserve_default=False,
        ),
    ]

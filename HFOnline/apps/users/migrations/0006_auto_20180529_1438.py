# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-05-29 14:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20180529_1350'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='birthday',
            new_name='birday',
        ),
    ]

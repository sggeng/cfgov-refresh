# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-02 22:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0221_reportsectionssidenav_report_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authornames',
            name='bio_link',
        ),
    ]

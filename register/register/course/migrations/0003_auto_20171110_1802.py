# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-10 18:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_auto_20171110_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='offered_to',
            field=models.CharField(choices=[('CS', 'Computer Science'), ('IT', 'Information Technology')], max_length=20, null=True),
        ),
    ]
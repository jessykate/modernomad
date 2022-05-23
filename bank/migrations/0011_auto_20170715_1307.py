# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-07-15 13:07
from __future__ import unicode_literals

from django.db import migrations


def create_drft(apps, schema_editor):
    Currency = apps.get_model('bank', 'Currency')
    Currency.objects.get_or_create(name='DRFT', defaults={'symbol': 'Ɖ'})

class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0010_auto_20170117_2150'),
    ]

    operations = [
        migrations.RunPython(create_drft, elidable=True),
    ]
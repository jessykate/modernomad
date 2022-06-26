# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-07-27 09:24
from __future__ import unicode_literals

from modernomad.core.forms import create_username
from django.db import migrations


def fix_usernames(User):
    for user in User.objects.all():
        tries = 1
        user.username = create_username(user.first_name, user.last_name)
        while User.objects.filter(username=user.username).count() > 0:
            tries = tries + 1
            user.username = create_username(user.first_name, user.last_name,
                                            suffix=tries)
        user.save()


def run_migration(apps, schema_editor):
    fix_usernames(apps.get_model('auth', 'User'))


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0070_auto_20170123_1158'),
    ]

    operations = [
        migrations.RunPython(run_migration, elidable=True),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2016-12-22 21:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0007_auto_20161221_1222'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'ordering': ['transaction__date'], 'verbose_name_plural': 'Entries'},
        ),
        migrations.AlterField(
            model_name='account',
            name='name',
            field=models.CharField(default='Some account', max_length=50),
            preserve_default=False,
        ),
    ]

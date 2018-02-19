# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-19 10:27
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0043_auto_20170808_1009'),
        ('order', '0016_auto_20180119_0903'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.BusinessClient', verbose_name='Business Client'),
        ),
    ]

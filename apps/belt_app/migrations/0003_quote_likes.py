# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-20 16:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('belt_app', '0002_quote'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='likes',
            field=models.ManyToManyField(related_name='liked_quotes', to='belt_app.User'),
        ),
    ]

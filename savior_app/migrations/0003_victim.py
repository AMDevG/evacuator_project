# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-28 23:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('savior_app', '0002_auto_20171028_0626'),
    ]

    operations = [
        migrations.CreateModel(
            name='Victim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('victimID', models.CharField(blank=True, default=None, max_length=3, null=True)),
                ('lat', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('lng', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('group_size', models.CharField(blank=True, default=None, max_length=2, null=True)),
                ('rescued', models.BooleanField(default=False)),
            ],
        ),
    ]
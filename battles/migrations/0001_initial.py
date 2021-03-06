# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-04 16:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Battle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('battle_number', models.CharField(blank=True, max_length=200, null=True)),
                ('attacker_king', models.CharField(blank=True, max_length=200, null=True)),
                ('defender_king', models.CharField(blank=True, max_length=200, null=True)),
                ('attacker_outcome', models.CharField(blank=True, max_length=200, null=True)),
                ('battle_type', models.CharField(blank=True, max_length=200, null=True)),
                ('major_death', models.IntegerField(blank=True, null=True)),
                ('major_capture', models.IntegerField(blank=True, null=True)),
                ('attacker_size', models.IntegerField(blank=True, null=True)),
                ('defender_size', models.IntegerField(blank=True, null=True)),
                ('attacker_commander', models.CharField(blank=True, max_length=200, null=True)),
                ('defender_commander', models.CharField(blank=True, max_length=200, null=True)),
                ('summer', models.CharField(blank=True, max_length=200, null=True)),
                ('location', models.CharField(blank=True, max_length=200, null=True)),
                ('region', models.CharField(blank=True, max_length=200, null=True)),
                ('note', models.TextField(blank=True, null=True)),
            ],
        ),
    ]

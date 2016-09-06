from __future__ import unicode_literals

from django.db import models


class Battle(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    battle_number = models.CharField(max_length=200, blank=True, null=True)
    attacker_king = models.CharField(max_length=200, blank=True, null=True)
    defender_king = models.CharField(max_length=200, blank=True, null=True)
    attacker_outcome = models.CharField(max_length=200, blank=True, null=True)
    battle_type = models.CharField(max_length=200, blank=True, null=True)
    major_death = models.IntegerField(blank=True, null=True)
    major_capture = models.IntegerField(blank=True, null=True)
    attacker_size = models.IntegerField(blank=True, null=True)
    defender_size = models.IntegerField(blank=True, null=True)
    attacker_commander = models.CharField(max_length=200, blank=True, null=True)
    defender_commander = models.CharField(max_length=200, blank=True, null=True)
    summer = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    region = models.CharField(max_length=200, blank=True, null=True)
    note = models.TextField(blank=True, null=True)

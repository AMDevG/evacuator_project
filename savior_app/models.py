# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Evacuator(models.Model):
        evacuatorID = models.CharField(max_length=3, null=True, blank=True, default=None)
        lat = models.CharField(max_length=20, null=True, blank=True, default=None)
        lng = models.CharField(max_length=20, null=True, blank=True, default=None)
        currentCapacity = models.CharField(max_length=2, null=True, blank=True, default=None)
        maxCapacity = models.CharField(max_length=2, null=True, blank=True, default=None)
        active = models.BooleanField(default=True)

        def __str__(self):
            return '{}'.format(self.evacuatorID)

class Victim(models.Model):
        victimID = models.CharField(max_length=3, null=True, blank=True, default=None)
        lat = models.CharField(max_length=20, null=True, blank=True, default=None)
        lng = models.CharField(max_length=20, null=True, blank=True, default=None)
        group_size= models.CharField(max_length=2, null=True, blank=True, default=None)
        rescued = models.BooleanField(default=False)

        def __str__(self):
            return '{}'.format(self.victimID)
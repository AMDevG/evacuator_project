# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Evacuator(models.Model):
        evacuatorID = models.CharField(max_length=3, null=True, blank=True, default=None)
        lat = models.CharField(max_length=3, null=True, blank=True, default=None)
        lng = models.CharField(max_length=3, null=True, blank=True, default=None)
        currentCapacity = models.CharField(max_length=3, null=True, blank=True, default=None)
        maxCapacity = models.CharField(max_length=3, null=True, blank=True, default=None)
        active = models.BooleanField(default=True)

        def __str__(self):
            return '{}'.format(self.name)
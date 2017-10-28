# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from savior_app.models import Evacuator, Victim

admin.site.register(Evacuator)
admin.site.register(Victim)
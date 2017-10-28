# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .models import Evacuator
from .serializers import EvacuatorSerializer
from rest_framework.response import Response
from django.core import serializers

class EvacuatorViewSet(viewsets.ModelViewSet):
	queryset = Evacuator.objects.all()
	serializer_class = EvacuatorSerializer
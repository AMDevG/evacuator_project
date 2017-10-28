# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .models import Evacuator
from .serializers import EvacuatorSerializer
from rest_framework.response import Response
from django.http import HttpResponse
from django.core import serializers
from geopy.distance import great_circle

class EvacuatorViewSet(viewsets.ModelViewSet):
	queryset = Evacuator.objects.all()
	serializer_class = EvacuatorSerializer


def process(request, name):


	print("Received vicID: ")
	print("Received vicName: ")

	return HttpResponse("Vic ID: %s"%name)


def calculateDistance(victimCoords, evacCords):
	return great_circle(victimCoords, evacCords).miles




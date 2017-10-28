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


def process(request, vicID, lat, lng, grpSize):
#def process(request, vicID, lat):
	print("VicID Passed: ", vicID)
	print("lat Passed: ", lat)
	print("lng Passed: ", lng)
	print("grpSize Passed: ", grpSize)

	findNearestEvacuator(grpSize)

	
	return HttpResponse("Vic ID: %s"%vicID)


def calculateDistance(victimCoords, evacCords):
	return great_circle(victimCoords, evacCords).miles



def testDB():
	for evacuator in Evacuator.objects.all():
		print("Evacuator ", evacuator.evacuatorID)


def findNearestEvacuator(grpSize):
	group_size = int(grpSize)
	available_evacuators = []
	min_dist = {}

	victimCoords = (45.679,-51.456)

	## Calculates evacs who have available space
	for evacuator in Evacuator.objects.all():
		capacity = int(evacuator.maxCapacity) - int(evacuator.currentCapacity)
		print("Capacity is ",capacity)
		if group_size <= capacity:
			print("Adding to available evacuator")
			available_evacuators.append(evacuator)
			
	for evacuator in available_evacuators:
		evac_coords = (evacuator.lat, evacuator.lng)

		if bool(min_dist) == False:
			print("Setting mindist")
			min_dist[evacuator.evacuatorID] = int(calculateDistance(victimCoords, evac_coords))

		else:
			print("Not first loop")
			current_distance = int(calculateDistance(victimCoords, evac_coords))

			for key in min_dist.keys():
				if current_distance < min_dist[key]:
					min_dist[evacuator.evacuatorID] = current_distance
					print("Changin min distance to: ", current_distance)

	print(min_dist)













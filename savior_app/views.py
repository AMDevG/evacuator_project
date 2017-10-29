# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .models import Evacuator, Victim
from .serializers import EvacuatorSerializer
from rest_framework.response import Response
from django.http import HttpResponse
from django.core import serializers
from geopy.distance import great_circle
import json

class EvacuatorViewSet(viewsets.ModelViewSet):
	queryset = Evacuator.objects.all()
	serializer_class = EvacuatorSerializer

def process(request, vicID, lat, lng, grpSize):
	victim_information = {}
	victim_coords = (lat, lng)
	new_victim = Victim.objects.create(victimID=vicID, lat=lat, lng=lng, group_size=grpSize)
	new_victim.save()

	json_evac_info = findNearestEvacuator(victim_coords, grpSize)

	return HttpResponse(json_evac_info, content_type="application/json")

def calculateDistance(victimCoords, evacCords):
	return great_circle(victimCoords, evacCords).miles

def findNearestEvacuator(victimCoords, grpSize):
	group_size = int(grpSize)
	available_evacuators = []
	
	min_dist = {}
	evacuator_info = {}
	selected_key = ""

	## Calculates evacs who have available space
	for evacuator in Evacuator.objects.all():
		capacity = int(evacuator.maxCapacity) - int(evacuator.currentCapacity)
		if group_size <= capacity:
			available_evacuators.append(evacuator)

	if len(available_evacuators) == 0:
		json_evac_info = json.dumps({})
		return json_evac_info

	
	##Calculates closest available evacuator
	for evacuator in available_evacuators:
		evac_coords = (evacuator.lat, evacuator.lng)

		if bool(min_dist) == False:
			print("Setting mindist")
			min_dist[evacuator.evacuatorID] = int(calculateDistance(victimCoords, evac_coords))
		else:
			current_distance = int(calculateDistance(victimCoords, evac_coords))
			for key in min_dist.keys():
				if current_distance < min_dist[key]:
					min_dist[evacuator.evacuatorID] = current_distance

	### Creates JSON dict of dispatched for http response 
	for key in min_dist:
		selected_key = key

	selected_evacuator = Evacuator.objects.get(evacuatorID=selected_key)
	new_capacity = int(selected_evacuator.currentCapacity) + group_size
	selected_evacuator.currentCapacity = str(new_capacity)
	selected_evacuator.save()
	
	evacuator_info = {"evacID": selected_evacuator.evacuatorID, "lat":selected_evacuator.lat, "lng":selected_evacuator.lng, "currentCapacity":selected_evacuator.currentCapacity, "maxCapacity":selected_evacuator.maxCapacity, "distance":min_dist[selected_key]}
	json_evac_info = json.dumps(evacuator_info)
	
	return json_evac_info


def testMap(request):

	victimCoords = []
	evacCoords = []

	for victim in Victim.objects.all():
		coords_array = [float(victim.lat), float(victim.lng)]
		victimCoords.append(coords_array)

	for evacuator in Evacuator.objects.all():
		coords_array = [float(evacuator.lat), float(evacuator.lng)]
		evacCoords.append(coords_array)

	return render(request, "map.html", {'victimCoords':victimCoords, 'evacCoords': evacCoords})




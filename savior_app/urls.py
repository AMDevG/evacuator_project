from django.conf.urls import url, include
#from django.urls import path

from . import views

urlpatterns = [
	url(r'^process/(?P<vicID>[\w\-]+)/(?P<lat>[-+]?([0-9]*\.[0-9]+|[0-9]+))/(?P<lng>[-+]?([0-9]*\.[0-9]+|[0-9]+))/(?P<grpSize>[0-9])/$', views.process, name="process")
	]

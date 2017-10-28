from django.conf.urls import url, include
#from django.urls import path

from . import views

urlpatterns = [
   #url(r'^process/(?P<string>[\w\-]+)/$', views.process, name="process")
   url(r'^process/(?P<name>[\w\-]+)/$', views.process, name="process")
]
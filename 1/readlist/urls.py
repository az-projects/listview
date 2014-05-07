from django.conf.urls import patterns, include, url
from models import *
from views import *
from django.contrib import admin

 

urlpatterns = patterns('',
  url(r'^admin/',include(admin.site.urls)),
  url(r'^hello/$',hello),
)

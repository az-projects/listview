
from django.conf.urls import patterns, include, url  
from models import *
from views import *

from django.contrib import admin 
admin.autodiscover()  

from readlist.views import syncdb 

urlpatterns = patterns('',
    url(r'^syncdb/', syncdb),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$',hello),
)

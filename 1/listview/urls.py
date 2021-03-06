from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns( '',
    # Examples:
    # url(r'^$', 'saetest.views.home', name='home'),
    # url(r'^saetest/', include('saetest.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
 )
urlpatterns += patterns ( '',
 url( r'^$', TemplateView.as_view( template_name = 'base.html' ) ),
 url( r'^readlist/', include( 'readlist.urls' ) ),
 url( r'^admin/', include( admin.site.urls ) ),
 url( r'^restframework', include( 'djangorestframework.urls', namespace = 'djangorestframework' ) ),
 )

urlpatterns += staticfiles_urlpatterns()

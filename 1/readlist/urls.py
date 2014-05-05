
from django.conf.urls.defaults import *
from models import *
from views import *
 

urlpatterns = patterns('',
  url(r'^hello/$',hello),
)

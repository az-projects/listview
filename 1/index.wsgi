import sae
from listview import wsgi

application = sae.create_wsgi_app(wsgi.application)

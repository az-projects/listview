import os,sys
app_root = os.path.dirname(__file__) 
sys.path.insert(0, os.path.join(app_root, 'BeautifulSoup-3.2.1'))
sys.path.insert(0, os.path.join(app_root, 'djangorestframework-0.4.0'))
sys.path.insert(0, os.path.join(app_root, 'requests-2.2.1')) 

import sae
from listview import wsgi

application = sae.create_wsgi_app(wsgi.application)

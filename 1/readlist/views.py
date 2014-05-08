from django.http  import Http404,HttpResponse,HttpResponseRedirect
#from django.template.loader import get_template
#from django.template import Context
from django.shortcuts import render_to_response
import sys
import StringIO   

def hello(request):
    
    return HttpResponse("hello world")# Create your views here.

def syncdb(request):  
    
    saveout = sys.stdout  
    log_out = StringIO.StringIO()    
    sys.stdout = log_out   
    from django.core.management import execute_from_command_line  
    execute_from_command_line(["manage.py", "syncdb", "--noinput"])  
    result = log_out.getvalue()  
    sys.stdout = saveout  
    return HttpResponse(result.replace("\n","<br/>")) 

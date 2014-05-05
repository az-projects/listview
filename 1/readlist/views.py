from django.http  import Http404,HttpResponse,HttpResponseRedirect
#from django.template.loader import get_template
#from django.template import Context
from django.shortcuts import render_to_response

def hello(request):
    
    return HttpResponse("hello world")# Create your views here.

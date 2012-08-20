from django.shortcuts import render_to_response
from django.template import RequestContext
# Create your views here.

def construction(request):
   return render_to_response("construction.html", [], context_instance=RequestContext(request))

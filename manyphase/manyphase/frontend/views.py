from django.shortcuts import render_to_response
from django.template import RequestContext
from manyphase.lead.models import PartialCustomerForm
# Create your views here.

def ajax(request):
   if request.method == 'GET':
       print request.get_full_path()
   return render_to_response("construction.html", {'form': PartialCustomerForm,}, context_instance=RequestContext(request))
    
def main(request):
   return render_to_response("main.html", {'form': PartialCustomerForm,}, context_instance=RequestContext(request))

def construction(request):
   return render_to_response("construction.html", {'form': PartialCustomerForm,}, context_instance=RequestContext(request))

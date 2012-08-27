from django.shortcuts import render_to_response
from django.template import RequestContext
from manyphase.lead.models import PartialCustomerForm
# Create your views here.

def construction(request):
   return render_to_response("construction.html", {'form': PartialCustomerForm,}, context_instance=RequestContext(request))

from django.shortcuts import render_to_response, HttpResponseRedirect
from django.template import RequestContext
from manyphase.lead.models import PartialCustomerForm, FullCustomerForm
# Create your views here.

def ajax(request):
   if request.method == 'GET':
       split_url = request.get_full_path().split("/")
       page = (split_url[len(split_url)-1]+".html").lower()


   return render_to_response(page, {'form': FullCustomerForm,}, context_instance=RequestContext(request))
    
def main(request):
   return render_to_response("main.html", {'form': FullCustomerForm,}, context_instance=RequestContext(request))

def construction(request):
   return render_to_response("construction.html", {'form': PartialCustomerForm,}, context_instance=RequestContext(request))

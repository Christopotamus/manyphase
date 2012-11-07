from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from models import Customer, PartialCustomerForm, FullCustomerForm

# Create your views here.
def addEmail(request):
    if request.method == 'POST':
        form = FullCustomerForm(request.POST)
        if form.is_valid():
            form_data= form.cleaned_data
            lead = form.save(commit=False)
            lead.save()
            return render_to_response("shortly.html", {"success":True}, context_instance=RequestContext(request))
        
    return HttpResponseRedirect('/') 


from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from models import Customer, PartialCustomerForm

# Create your views here.
def addEmail(request):
    if request.method == 'POST':
        form = PartialCustomerForm(request.POST)
        if form.is_valid():
            form_email = form.cleaned_data['email']
            lead = Customer.objects.create(email=form_email)
            lead.save()
            return render_to_response("shortly.html", {"success":True}, context_instance=RequestContext(request))
        
    return HttpResponseRedirect('/') 


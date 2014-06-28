from django.shortcuts import render, render_to_response, RequestContext
from django.contrib import messages

# Create your views here.

from .forms import DriveoffForm, RegoSearchForm
from .models import Driveoff

def home(request):

    form = RegoSearchForm(request.POST or None)

    if form.is_valid():
        rego_to_search = form.cleaned_data['rego']
        #query db .. send a message if we get a hit
        driveoffs = Driveoff.objects.filter(rego=rego_to_search)
        
        if not driveoffs:
          messages.success(request, 'YES OK')
        else:
          messages.warning(request, 'DO NOT AUTHORISE!')
          #loop through all driveoffs and send multiple messages

    return render_to_response("driveoff.html",
                                locals(),
                                context_instance=RequestContext(request))

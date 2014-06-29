from django.shortcuts import render, render_to_response, RequestContext
from django.contrib import messages
from datetime import date, datetime

# Create your views here.

from .forms import DriveoffForm, RegoSearchForm
from .models import Driveoff

def home(request):

    form = RegoSearchForm(request.POST or None)

    if form.is_valid():
        rego_to_search = form.cleaned_data['rego']
        #query db .. send a message if we get a hit
        driveoffs = Driveoff.objects.filter(rego__iexact=rego_to_search)
        
        if not driveoffs:
          messages.success(request, 'YES OK')
        else:
          messages.warning(request, 'DO NOT AUTHORISE!')
          #loop through all driveoffs and send multiple messages
          make=model=colour = "<unknown>"
          for driveoff in driveoffs:
            if driveoff.make:
                make = driveoff.make 
            if driveoff.model:
                model = driveoff.model 
            if driveoff.colour:
                colour = driveoff.colour 
            date = driveoff.timestamp.strftime(format='%d-%m-%Y')

            msg = 'Car Rego: %s, Owing: $%s at site: %s, reported: %s. (Make: %s, Model: %s, Colour: %s)' \
                    % (driveoff.rego, driveoff.amount, driveoff.site, date, make, model, colour)

            messages.error(request, msg)

    return render_to_response("driveoff.html",
                                locals(),
                                context_instance=RequestContext(request))

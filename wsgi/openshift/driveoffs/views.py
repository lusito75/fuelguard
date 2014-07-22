from django.shortcuts import render, render_to_response, RequestContext
from django.contrib import messages
from datetime import date, datetime

# Create your views here.

from .forms import DriveoffForm, RegoSearchForm
from .models import Driveoff

def home(request):

    form = RegoSearchForm(request.POST or None)

    if form.is_valid():
        rego_to_search   = form.cleaned_data['rego']
        colour_to_search = form.cleaned_data['colour']
        make_to_search   = form.cleaned_data['make']
        model_to_search  = form.cleaned_data['model']
        #query db .. send a message if we get a hit
        driveoffs = Driveoff.objects.filter(rego__iexact=rego_to_search)
        maybe_driveoffs = Driveoff.objects.filter(
                                                rego__icontains=rego_to_search
                                         ).filter(
                                                colour__icontains=colour_to_search
                                         ).filter(
                                                make__icontains=make_to_search
                                         ).filter(
                                                model__icontains=model_to_search
                                         )
        
        if not driveoffs and not maybe_driveoffs:
          messages.success(request, 'YES OK')
        elif driveoffs:
          messages.warning(request, 'DO NOT AUTHORISE!')
          #loop through all driveoffs and send multiple messages
          for driveoff in driveoffs:
            msg = build_msg(driveoff)
            messages.error(request, msg)
        elif maybe_driveoffs:
          messages.info(request, 'POSSIBLE MATCHES')
          for possible in maybe_driveoffs:
            msg = build_msg(possible)
            messages.info(request, msg)

    return render_to_response("driveoff.html",
                                locals(),
                                context_instance=RequestContext(request))


def build_msg(driveoff):
  make=model=colour = "<unknown>"
  if driveoff.make:
      make = driveoff.make 
  if driveoff.model:
      model = driveoff.model 
  if driveoff.colour:
      colour = driveoff.colour 
  date = driveoff.timestamp.strftime(format='%d-%m-%Y')
  msg = 'Car Rego: %s, Owing: $%s at site: %s, reported: %s. (Make: %s, Model: %s, Colour: %s)' \
            % (driveoff.rego, driveoff.amount, driveoff.site, date, make, model, colour)
  return msg


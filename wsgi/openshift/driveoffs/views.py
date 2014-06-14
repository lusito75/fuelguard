from django.shortcuts import render, render_to_response, RequestContext
from django.contrib import messages

# Create your views here.

from .forms import DriveoffForm, RegoSearchForm

def home(request):

    form = RegoSearchForm(request.POST or None)

    if form.is_valid():
        #save_it = form.save(commit=False)
        #save_it.save()
        #query db .. send a message if we get a hit
        messages.success(request, 'YES OK')

    return render_to_response("driveoff.html",
                                locals(),
                                context_instance=RequestContext(request))

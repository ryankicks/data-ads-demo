import json
# TODO: Fix * imports
from django.shortcuts import *
from django.contrib.auth.decorators import login_required, user_passes_test
from django.conf import settings

@login_required
def handler(request):
    """
    Returns account page handler page for given request
    """
    context = {"request": request}
    return render_to_response('audiences.html', context, context_instance=RequestContext(request))

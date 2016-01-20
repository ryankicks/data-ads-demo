import json
# TODO: Fix * imports
from django.shortcuts import *
from django.contrib.auth.decorators import login_required, user_passes_test
from django.conf import settings
from twitter_ads.client import Client
from twitter_ads.audience import TailoredAudience
from twitter_ads.http import Request
from twitter_ads.cursor import Cursor

@login_required
def handler(request):
    """
    Returns account page handler page for given request
    """
    context = {"request": request}
    return render_to_response('audiences.html', context, context_instance=RequestContext(request))

@login_required
def new(request):
    """
    Returns a new TA path to hold the bucket location.
    """
    client = Client(settings.SOCIAL_AUTH_TWITTER_KEY, settings.SOCIAL_AUTH_TWITTER_SECRET, settings.TWITTER_ACCESS_TOKEN, settings.TWITTER_ACCESS_TOKEN_SECRET)
    account_id = request.REQUEST.get("account_id", "")
    name = request.REQUEST.get("name", "")
    resource = '/0/accounts/' + account_id + '/tailored_audiences'
    params = {'name': name, 'list_type': 'HANDLE'}
    request = Request(client, 'post', resource, params=params).perform()
    # return audience.id to use
    ta_id = request.body['data']['id']
    json_data = {"account_id": account_id, "name": name, "id": str(ta_id)}
    return HttpResponse(json.dumps(json_data), content_type="application/json")

@login_required
def change(request):
    """
    Returns a change to TA to upload a bucket location.
    """
    client = Client(settings.SOCIAL_AUTH_TWITTER_KEY, settings.SOCIAL_AUTH_TWITTER_SECRET, settings.TWITTER_ACCESS_TOKEN, settings.TWITTER_ACCESS_TOKEN_SECRET)
    account_id = request.REQUEST.get("account_id", "")
    identifier = request.REQUEST.get("id", "")
    input_file_path = request.REQUEST.get("input_file_path", "")
    # Update With location
    resource = '/0/accounts/' + account_id + '/tailored_audience_changes'
    params = {'tailored_audience_id': identifier, 'input_file_path': input_file_path, 'operation': "ADD"}
    request = Request(client, 'post', resource, params=params).perform()
    json_data = {"account_id": account_id, "data": request.body['data']}
    return HttpResponse(json.dumps(json_data), content_type="application/json")

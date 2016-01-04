import json
# TODO: Fix * imports
from django.shortcuts import *
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import logout as auth_logout
from django.conf import settings
from twitter_ads.client import Client

@login_required
def json_handler(request):
    """
    Returns json_data {"campaigns": [campaign_list} for given request
    """

    client = Client(settings.SOCIAL_AUTH_TWITTER_KEY, settings.SOCIAL_AUTH_TWITTER_SECRET, settings.TWITTER_ACCESS_TOKEN, settings.TWITTER_ACCESS_TOKEN_SECRET)
    account_id = request.REQUEST.get("account_id", "")
    account = client.accounts(account_id)
    # TODO: Link to Ads API Docs for Campaign.rst
    campaigns = account.campaigns()
    campaign_list = []
    for campaign in campaigns:
        name = campaign.name
        identifier = campaign.id
        campaign_list.append({"name": name, "id": identifier})
    return HttpResponse(json.dumps({"account_id": account_id, "campaigns": campaign_list}), content_type="application/json")

@login_required
def handler(request):
    """
    Returns account page handler page for given request
    """
    account_id = request.REQUEST.get("account_id", "")
    context = {"request": request, "account_id": account_id}
    return render_to_response('campaigns.html', context, context_instance=RequestContext(request))

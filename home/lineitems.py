import json
# TODO: Fix * imports
from django.shortcuts import *
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import logout as auth_logout
from django.conf import settings
from twitter_ads.client import Client

@login_required
def new_targeting(request):
    """
    Creates a new
    """
    line_item_id = request.REQUEST.get("line_item_id", "")
    account_id = request.REQUEST.get("account_id", "")
    targeting_value = request.REQUEST.get("targeting_value");
    targeting_type = "BROAD_KEYWORD"

    client = Client(settings.SOCIAL_AUTH_TWITTER_KEY, settings.SOCIAL_AUTH_TWITTER_SECRET, settings.TWITTER_ACCESS_TOKEN, settings.TWITTER_ACCESS_TOKEN_SECRET)
    account = client.accounts(account_id)

    targeting_criteria = TargetingCriteria(account)
    targeting_criteria.line_item_id = line_item.id
    targeting_criteria.targeting_type = targeting_type
    targeting_criteria.targeting_value = targeting_value
    targeting_criteria.save()

    return HttpResponse(json.dumps({"account_id": account_id, "line_item_id": line_item_id, "targeting_value": targeting_value}), content_type="application/json")

@login_required
def new(request):
    """
    Returns a new campaign
    """
    client = Client(settings.SOCIAL_AUTH_TWITTER_KEY, settings.SOCIAL_AUTH_TWITTER_SECRET, settings.TWITTER_ACCESS_TOKEN, settings.TWITTER_ACCESS_TOKEN_SECRET)
    account_id = request.REQUEST.get("account_id", "")
    campaign_id = request.REQUEST.get("campaign_id", "")
    name = request.REQUEST.get("name", "")
    budget = request.REQUEST.get("budget", "")
    account = client.accounts(account_id)

    # create your campaign
    line_item = LineItem(account)
    line_item.campaign_id = campaign.id
    line_item.name = name
    line_item.product_type = PRODUCT.PROMOTED_TWEETS
    line_item.placements = [PLACEMENT.ALL_ON_TWITTER]
    line_item.objective = OBJECTIVE.TWEET_ENGAGEMENTS
    line_item.bid_amount_local_micro = 10000
    line_item.paused = True
    line_item.save()

    json_data = {"account_id": account_id, "campaign_name": campaign_name, "campaign_id": campaign.id}
    return HttpResponse(json.dumps(json_data), content_type="application/json")

@login_required
def json_handler(request):
    """
    Returns json_data {"campaigns": [campaign_list} for given request
    """

    client = Client(settings.SOCIAL_AUTH_TWITTER_KEY, settings.SOCIAL_AUTH_TWITTER_SECRET, settings.TWITTER_ACCESS_TOKEN, settings.TWITTER_ACCESS_TOKEN_SECRET)
    account_id = request.REQUEST.get("account_id", "")
    campaign_id = request.REQUEST.get("campaign_id", "")
    account = client.accounts(account_id)
    # TODO: Link to Ads API Docs for LineItem.rst
    line_items = account.line_items(None, params={'campaign_id': campaign_id})
    line_item_list = []
    for line_item in line_items:
        name = line_item.name
        identifier = line_item.id
        objective = line_item.objective
        bid_amount = line_item.bid_amount_local_micro
        # Sometimes Bid Amount is None
        if bid_amount != None:
            bid_amount = bid_amount/10000
        line_item_list.append({"name": name, "id": identifier, "objective": objective, "bid_amount": bid_amount})
    return HttpResponse(json.dumps({"account_id": account_id, "campaign_id": campaign_id, "line_items": line_item_list}), content_type="application/json")

@login_required
def handler(request):
    """
    Returns account page handler page for given request
    """
    account_id = request.REQUEST.get("account_id", "")
    campaign_id = request.REQUEST.get("campaign_id", "")
    context = {"request": request, "account_id": account_id, "campaign_id": campaign_id}
    return render_to_response('lineitems.html', context, context_instance=RequestContext(request))
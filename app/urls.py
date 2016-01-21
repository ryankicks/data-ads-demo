from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from app import settings

urlpatterns = patterns('',
    url(r'^$', 'home.views.login', name='login'),
    url(r'^home$', 'home.views.home', name='home'),
    url(r'^logout$', 'home.views.logout', name='logout'),
    url(r'^query/chart', 'home.views.query_chart', name='query_chart'),
    url(r'^query/tweets', 'home.views.query_tweets', name='query_tweets'),
    url(r'^query/frequency', 'home.views.query_frequency', name='query_frequency'),

    # ADS API Handlers
    url(r'^ads/accounts', 'home.accounts.handler', name='ads_accounts'),
    url(r'^ads/api/accounts', 'home.accounts.json_handler', name='ads_api_accounts'),

    # ADS API Campaigns
    url(r'^ads/campaigns', 'home.campaigns.handler', name='ads_campaigns'),
    url(r'^ads/api/campaigns', 'home.campaigns.json_handler', name='ads_api_campaigns'),
    url(r'^ads/api/campaign/new', 'home.campaigns.new', name='ads_api_campaign_new'),

    # ADS API LineItems
    url(r'^ads/line_items', 'home.lineitems.handler', name='ads_line_items'),
    url(r'^ads/api/line_items', 'home.lineitems.json_handler', name='ads_api_line_items'),
    url(r'^ads/api/line_item/new', 'home.lineitems.new', name='ads_api_line_item_new'),

    # ADS API Targeting
    url(r'^ads/api/targeting/new', 'home.lineitems.new_targeting', name='ads_api_new_targeting'),

    # ADS API Audiences
    url(r'^ads/audiences', 'home.audiences.handler', name='ads_audiences'),
    url(r'^ads/api/audiences/new', 'home.audiences.new', name='ads_audiences_new'),
    url(r'^ads/api/audiences/change', 'home.audiences.change', name='ads_audiences_change'),


    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
 (r'^static/(.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
 )

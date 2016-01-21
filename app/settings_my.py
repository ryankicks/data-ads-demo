try:
    from app.settings import *
except ImportError, exp:
    pass

SOCIAL_AUTH_TWITTER_KEY = 'sw5evtqO3gbh0yZceH1B6gGR4'
SOCIAL_AUTH_TWITTER_SECRET = 'VJSyKC6HTp9JwbF3x7LUYEPmdQ2UTGlUw4fJkUIqkTBmho85UC'

TWITTER_ACCESS_TOKEN = '15313098-4TwY1wIlWpQO90Is0cNKCr774V8yCEjCgoepfTyMX'
TWITTER_ACCESS_TOKEN_SECRET = 'cP44KHGZ8NzHN0HWNGbY69kPAXpjjyAKs4jXKLXdidpE4'

GNIP_USERNAME = 'rchoi+gnip@twitter.com'
GNIP_PASSWORD = 'BigData1'
GNIP_SEARCH_ENDPOINT = 'https://data-api.twitter.com/search/fullarchive/accounts/dpr-content/InternalSearchDemo2.json'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

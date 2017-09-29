import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

PROJECT_BASE_DIR = os.path.dirname(BASE_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'lbbdmm7*j7_mm$64&1lz)f-)i196ivv&t-r#nv#at525@5i=pr'


ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'social.apps.django_app.default',

    'pipeline',
    'storages',

    'rest_framework',
    'haystack',
    'watson',

    'versatileimagefield',

    'wef',
    'users',
    'items',

    'elasticstack',

    'raven.contrib.django.raven_compat',
]


MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'social.apps.django_app.middleware.SocialAuthExceptionMiddleware',
]


ROOT_URLCONF = 'wef.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social.apps.django_app.context_processors.backends',
                'social.apps.django_app.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'wef.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Celery Broker Init
BROKER_URL = 'redis://localhost:6379/0'

# Django haystack
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'elasticstack.backends.ConfigurableElasticSearchEngine',
        'URL': 'http://127.0.0.1:9200/',
        'INDEX_NAME': 'bookconnect_elastic_index',
    },
}

ELASTICSEARCH_DEFAULT_ANALYZER = 'korean_index'

ELASTICSEARCH_INDEX_SETTINGS = {
  'settings': {
      "analysis": {
          "analyzer": {
              "korean_index": {
                  "type": "custom",
                  "tokenizer": "mecab_ko_standard_tokenizer"
              },
              "korean_query": {
                  "type": "custom",
                  "tokenizer": "korean_query_tokenizer"
              },
              "ngram_analyzer": {
                  "type": "custom",
                  "tokenizer": "standard",
                  "filter": ["haystack_ngram", "lowercase"]
              },
              "edgengram_analyzer": {
                  "type": "custom",
                  "tokenizer": "standard",
                  "filter": ["haystack_edgengram", "lowercase"]
              }
          },
          "tokenizer": {
              "korean_query_tokenizer": {
                  "type": "mecab_ko_standard_tokenizer",
                  "compound_noun_min_length": 100
              },
              "haystack_ngram_tokenizer": {
                  "type": "nGram",
                  "min_gram": 3,
                  "max_gram": 15,
              },
              "haystack_edgengram_tokenizer": {
                  "type": "edgeNGram",
                  "min_gram": 2,
                  "max_gram": 15,
                  "side": "front"
              }
          },
          "filter": {
              "haystack_ngram": {
                  "type": "nGram",
                  "min_gram": 3,
                  "max_gram": 15
              },
              "haystack_edgengram": {
                  "type": "edgeNGram",
                  "min_gram": 2,
                  "max_gram": 15
              }
          }
      }
  }
}
